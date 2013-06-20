#!/usr/bin/env python
# Copyright (c) 2013 Alon Swartz <alon@turnkeylinux.org>
"""Sort TurnKey Linux Appliance Candidates by stupid scoring algorithm"""

import re
import os
import sys
import getopt

def fatal(e):
    print >> sys.stderr, 'Error: ' + str(e)
    sys.exit(1)

def usage(e=None):
    if e:
        print >> sys.stderr, 'Error: ' + str(e)

    print >> sys.stderr, 'Syntax: %s path/to/Candidates.md' % sys.argv[0]
    print >> sys.stderr, __doc__.strip()

    sys.exit(1)

class Error(Exception):
    pass

class AttrDict(dict):
    """Attribute Dictionary (set and access attributes 'pythonically')"""
    def __getattr__(self, name):
        if name in self:
            return self[name]
        raise AttributeError('no such attribute: %s' % name)

    def __setattr__(self, name, val):
        self[name] = val

class Candidate(AttrDict):
    def __init__(self):
        self.name = None
        self.description = None
        self.labels = []
        self.supporters = []
        self.resources = []

    @property
    def score(self):
        i = 0
        if self.description:
            i += 1
        if len(self.labels) > 0:
            i += 1
        if 'tklpatch' in self.labels:
            i += 1
        if len(self.supporters) > 2:
            i += 2
        if len(self.resources) > 1:
            i += 1

        return i

    @property
    def title(self):
        s = self.name
        if self.description:
            s += ': %s' % self.description
        if self.labels:
            s += ' (' + ', '.join(self.labels) + ')'

        return s

    def __str__(self):
        s = '### %s\n' % self.title
        if self.supporters or self.resources:
            s += '\n'
        if self.supporters:
            s += '* Supporters: %s\n' % ', '.join(self.supporters)
        for resource in self.resources:
            s += '* %s\n' % resource

        return s

def parse_candidates(path):
    candidates = []
    c = Candidate()
    for line in file(path, 'r').readlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith('###'):
            if c.name:
                candidates.append(c)

            c = Candidate()
            m = re.match('### (.*): (.*) \((.*)\)', line)
            if m:
                c.name = m.groups()[0].strip()
                c.description = m.groups()[1].strip()
                for label in m.groups()[2].split(','):
                    c.labels.append(label.strip())
                continue

            m = re.match('### (.*) \((.*)\)', line)
            if m:
                c.name = m.groups()[0].strip()
                for label in m.groups()[1].split(','):
                    c.labels.append(label.strip())
                continue

            m = re.match('### (.*): (.*)', line)
            if m:
                c.name = m.groups()[0].strip()
                c.description = m.groups()[1].strip()
                continue

            m = re.match('### (.*)', line)
            if m:
                c.name = m.groups()[0].strip()
                continue

            raise Error('parsing failed: %s' % line)

        elif line.startswith('* Supporters:'):
            line = line.lstrip('* Supporters:')
            for supporter in line.split(','):
                c.supporters.append(supporter.strip())

        elif line.startswith('* '):
            c.resources.append(line.lstrip('* '))

        else:
            raise Error('parsing failed: %s' % line)

    candidates.append(c)
    return candidates

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError, e:
        usage(e)

    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()

    if len(args) == 0:
        usage()

    if len(args) != 1:
        usage('incorrect number of arguments')

    path = args[0]
    if not os.path.exists(path):
        fatal('path does not exist: %s' % path)

    candidates = parse_candidates(path)
    candidates = sorted(candidates, key=lambda c: c.score, reverse=True)

    for c in candidates:
        print c

if __name__ == '__main__':
   main()
