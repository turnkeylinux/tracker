Recommended RST Document Style
==============================

This document is basically a cheat sheet for reStructuredText to help guide new people in following TurnKeyLinux's documenting style.

Contents
--------

* `Headers <#Headers>`_

* `Horizontal Rules <#horizontal-rules>`_

* `Code Formatting <#code-formatting>`_

* `Basic Formatting <#basic-formatting>`_

* `Code Blocks <#code-blocks>`_

* `Escaping Markup <#escaping-markup>`_

* `Lists <#Lists>`_

* `Hyperlink URLs <#hyperlink-urls>`_

* `References <#references>`_

Headers
-------

Typically ``Header 1`` is used for README.rst, any additional documentation pages will start with ``Header 2``, then ``Header 3`` for page sections and ``Header 4`` for subsections. ``Header 5`` is rarely used.

The underlining needs to be atleast as long as the text

Example of headers::

    ========
    Header 1
    ========

    Header 2
    ========

    Header 3
    --------

    Header 3 with a longer text
    ---------------------------

    Header 4
    ^^^^^^^^

    Header 5
    """"""""

Code Formatting
---------------

To use ``highlighted monospaced text``, prepend and append the text with a double backquote (``).

For example:

Change into directory with \``cd /etc/\`` and show a long list of of the directory with \``ls -l\``.

Change into directory with ``cd /etc/`` and show a long list of of the directory with ``ls -l``.

Basic Formatting
----------------

``*italic text*``

*italic text*

``**bold text**``

**bold text**

Code Blocks
-----------

Follow a sentence or paragraph with a double colon (``::``) and indent the next line 1 tab or four spaces to create a monospaced highlighted block of text.

For example::

    the quick brown fox jumps over the lazy dog::

        the quick brown fox jumps over the lazy dog
        the quick brown fox jumps over the lazy dog

the quick brown fox jumps over the lazy dog::

    the quick brown fox jumps over the lazy dog
    the quick brown fox jumps over the lazy dog

Escaping Markup
---------------

Occassionally you will want to use markup characters just as them themselves and without being interpreted. Markup characters are not interpreted when used within double backquotes or within a code block. In other contexts, you can precede the markup character with a backslash (\\) to escape the interpretation. This also applies to the backslash itself.

For example:

``\*This\* is not *italic* and \**this\** is not **bold**.``

\*This\* is not *italic* and \**this\** is not **bold**.

Lists
-----
Numbered
^^^^^^^^

Create a numbered list with ``#``.

For example::

    #. First item
    #. Second item
    #. Third item
        #. Frist sub item
        #. Second sub item
    #. Fourth item

#. First item
#. Second item
#. Third item
    #. Frist sub item
    #. Second sub item
#. Fourth item

Bullet
^^^^^^

Create a bullet point list with ``*``.

For example::

    * First item
    * Second item
      that continues on a second line
    * Third item
        * Use nested lists
        * By indenting two spaces
    * Fourth item

* First item
* Second item
  that continues on a second line
* Third item
    * Use nested lists
    * By indenting 4-7 spaces
* Fourth item

Hyperlink URLs
--------------

Hyperlinks can be created by prepending and appending with a single backqoute (`````) and including the reference or link at the end in angle brackets (``<>``) followed by the underscore (``_``).

You can also create links that reference a list at the bottom of the page. Using double full stop and a space (``..``) will hide the reference text from being displayed.

For example::

    * `Issue Tracker`_
    * `Wiki`_
    * `Support Forum`_
    * `General Discussion Forum`_
    * `Guidelines and Walk Through`_
    
    .. _Issue Tracker: https://github.com/turnkeylinux/tracker/issues/
    .. _Wiki: https://github.com/turnkeylinux/tracker/wiki/
    .. _support forum: http://www.turnkeylinux.org/forum/support/
    .. _general discussion forum: http://www.turnkeylinux.org/forum/general/
    .. _guidelines and walk through: https://github.com/turnkeylinux/tracker/blob/master/GITFLOW.rst

* `Issue Tracker`_
* `Wiki`_
* `Support Forum`_
* `General Discussion Forum`_
* `Guidelines and Walk Through`_

.. _Issue Tracker: https://github.com/turnkeylinux/tracker/issues/
.. _Wiki: https://github.com/turnkeylinux/tracker/wiki/
.. _support forum: http://www.turnkeylinux.org/forum/support/
.. _general discussion forum: http://www.turnkeylinux.org/forum/general/
.. _guidelines and walk through: https://github.com/turnkeylinux/tracker/blob/master/GITFLOW.rst

You can link to a file in the same repo.

```Follow TurnKeyLinux Workflow using git and GitHub <GITFLOW.rst>`_``

`Follow TurnKeyLinux Workflow using git and GitHub <GITFLOW.rst>`_



References
----------

https://gist.github.com/dupuy/1855764
https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst