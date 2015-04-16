Recommended Git Flow
====================

All TurnKey source code is managed by `git`_, and hosted on 
`GitHub`_ in one of the following organizations:

* `turnkeylinux`_: TurnKey related components and projects.
* `turnkeylinux-apps`_: TurnKey appliances.

Not only is `GitHub`_ used to host the source code, but also to
facilitate collaboration via `forks`_ and `pull requests`_. 

There are infinate ways to develop with git, but when teams and
collaborators are involved it's recommended to follow some sort of flow
and guidelines. The most widely acceptable flows are `git-flow`_ and
`GitHub flow`_.

Guidelines
----------

TurnKey related development is loosly based on the GitHub flow, and
follows these guidelines:

* Anything in the master branch is deployable - builds successfully and
  is tested to work.
* When working on something new, whether it be a bugfix or new feature,
  create a descriptively named branch off of master. Each new branch 
  should address just one issue (i.e. create a separate branch from 
  master for each issue).
* Commit to that branch locally and regularly. Source code should be
  documented and rational for changes included in commits.
* When you need feedback or help, or you think the branch is ready for
  merging, open a pull request.
* After someone else has reviewed and signed off on the changes, the
  project maintainer or a core developer will perform the merge in the
  official repository.
* Once it is merged and pushed to master, the project should be rebuilt
  and released immediately.

Walk through
------------

As described above, GitHub is used to facilitate collaboration, so the
first thing to do is create a `GitHub account`_ and add your SSH public
key if you haven't already done so.

Fork and clone the source
'''''''''''''''''''''''''

Next, fork the project you want to hack on:

* Log into `GitHub`_, and browse to the projects repository.
* Click the ``fork`` button.

That's it. You've successfully forked the project repository, but so far
it only exists on GitHub.

To be able to work on the project you'll need to clone it::

    git clone git@github.com:USERNAME/PROJECTNAME.git

So far so good. When a repository is cloned, it has a default ``remote``
called ``origin`` that points to your fork on GitHub, not the original
repository it was forked from.

To keep track of the original repository, you need to add another
remote, we'll call it ``upstream``::

    cd PROJECTNAME
    git remote add upstream https://github.com/ORGANIZATION/PROJECTNAME.git

    # Fetch any new changes to the original repository
    git fetch upstream

    # Merge any changes fetched into your working branch
    git merge upstream/master

Make your changes
'''''''''''''''''

* **Create a branch**: Note that you have only one ``pull request`` per branch::

    git checkout -b DESCRIPTIVE_BRANCH_NAME

* **Hack away**: Make your changes, test and commit as you go. Remember please only address one issue per branch/pull request
* **Test**: Perform final testing.

Push changes and submit a Pull Request
''''''''''''''''''''''''''''''''''''''

Now that you're finished hacking and all changes are committed, you need
to push them to your GitHub repository::

    git push origin DESCRIPTIVE_BRANCH_NAME

Last thing to do is send a ``pull request`` so the maintainer or one of
the core developers can review, sign off, and perform the merge in the
official repository.

* Browse to https://github.com/USERNAME/PROJECTNAME/tree/DESCRIPTIVE_BRANCH_NAME
* Click ``Pull Request``, describe the change and click ``Send pull request``.

Hooray! You did it.

If for some reason the maintainer or one of the core developers has a
problem with your change, they won't want to merge until fixed.

The good news is that whenever you commit and push more changes to that
branch of your code, they will be included in that original pull request
until it is closed.


.. _git: http://git-scm.com/documentation
.. _GitHub: https://github.com
.. _turnkeylinux: https://github.com/turnkeylinux
.. _turnkeylinux-apps: https://github.com/turnkeylinux-apps
.. _forks: https://help.github.com/articles/fork-a-repo
.. _pull requests: https://help.github.com/articles/using-pull-requests
.. _git-flow: http://nvie.com/posts/a-successful-git-branching-model
.. _GitHub flow: http://scottchacon.com/2011/08/31/github-flow.html
.. _GitHub account: https://github.com/signup

