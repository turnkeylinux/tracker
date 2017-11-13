# Contributing to TurnKey

The following is a consolidated series of guidelines for contributions to TurnKey Linux (TKL). These guidelines are derived from a number of existing documents that are currently spread across GitHub and the [documentation](https://www.turnkeylinux.org/docs) section of the TKL website. If you feel that these guidelines are lacking, feel free to make changes as you see fit.


## Contents

[General Information](#general-information)
* [About TurnKey Linux](#about-turnkey-linux)
* [Development Toolchain](#development-toolchain)

[Contributing](#contributing)
* [GitFlow](#gitflow)
* [Contribution Walkthrough](#contribution-walkthrough)
* [Bug reports and feature requests](#bug-reports-and-feature-requests)

## General Information

### About TurnKey Linux

TurnKey GNU/Linux is an open source library of Debian based system images packaged as virtual appliances. Virtual appliances function as self contained systems that are capable of running on industry standard hardware or virtual machines created through software such as Virtualbox. Consult [this guide](https://www.turnkeylinux.org/docs/installation-appliances-virtualbox-new) for a basic overview on how to install virtual appliances.

All TKL source code is managed by [Git](https://git-scm.com/documentation) and hosted here on GitHub under either:
* [turnkeylinux](https://github.com/turnkeylinux) for TurnKey related components and projects.
* [turnkeylinux-apps](https://github.com/turnkeylinux-apps) for TurnKey appliances.

Developers with good ideas are encouraged to be bold and contribute code.

### Development Toolchain

* [TKLDev](https://www.turnkeylinux.org/tkldev): This is the recommended tool for appliance development. As "the mother of all TurnKey apps", TKLDev is a self contained appliance that is capable of rapidly prototyping new Linux distributions and building existing integrations from source material. For more detailed information on using this appliance, consult the docs in the [TKLDev repository](https://github.com/turnkeylinux-apps/tkldev/tree/master/docs) here on GitHub.
* [TKLPatch](https://www.turnkeylinux.org/docs/tklpatch): A set of shell scripts that may be used to customize and extend existing virtual appliances. While recent versions of TKLDev enable the creation of appliances from source, TKLPatch may still be used for light customization.

## Contributing

### Gitflow

Development of TKL is loosely based on [GitHub Flow](http://scottchacon.com/2011/08/31/github-flow.html), a widely accepted set of guidelines for contributing to projects over GitHub. As such, TKL development follows these basic guidelines: 
* Anything in the master branch is deployable (builds that have successfully been proven to work)
* When working on something new (ie: a bugfix or a new feature), create a descriptively named branch off of the master. Each new branch should address a single issue. 
* Commit to that branch locally and regularly. Source code should be documented and rational for changes included in commits.
* Open a pull request for help, feedback or branch merging.
* Once someone else has reviewed and signed off on the changes, the project maintainer or a core developer will merge it with the official repository.
* Once it is merged and pushed to the master, the project should be rebuilt and released immediately. 

Collaboration is facilitated over GitHub through the use of [fork](https://help.github.com/articles/fork-a-repo/) and [pull requests](https://help.github.com/articles/using-pull-requests/).In order to make use of these features, developers will need to [create a GitHub account]() and add their SSH public key if they have not already done so.

### Contribution Walkthrough

**Fork and clone source:**
* To begin, login and find a repository that you would like to work on.
* Within the desired repository, press the ``fork`` button to fork the repository. 
* The repository will then need to be cloned before you can work on it. You can do so with this snippet of code:

   `git clone git@github.com:USERNAME/PROJECTNAME.git`

* Once the repository has been cloned, it will have a ``remote`` called ``origin``. This will point to your newly created fork on GitHub rather than the original repository.
*You will need to add another ``remote`` in order to keep track of the original repository. In this example, it will be called ``upstream``:

```
cd PROJECTNAME
git remote add upstream https://github.com/ORGANIZATION/PROJECTNAME.git
# Fetch any new changes to the original repository
git fetch upstream
# Merge any changes fetched into your working branch
git merge upstream/master
```

**Make your changes:**

* Create a branch with a descriptive name related to your changes. Note that you are limited to one ``pull request`` per branch.

    `git checkout -b DESCRIPTIVE_BRANCH_NAME`

* Make your changes, testing and committing as you progress. Remember to only address one issue per branch / pull request.
* Perform final testing before pushing any changes.

**Push changes and submit a pull request:**

Now that you're finished and all changes are committed, you need to push them to your GitHub repository:

    `git push origin DESCRIPTIVE_BRANCH_NAME`

Finally, submit a ``pull request``so that the maintainer or a core developer may review your changes and merge them into the official repository.If for some reason the maintainer or one of the core developers has a problem with your change, they won't want to merge until fixed. However, whenever you commit and push more changes to that branch of your code, they will be included in that original pull request until it is closed.

### Bug Reports and feature requests

TKL uses GitHub's project management features to track development. Included in these features are the [issue tracker](https://github.com/turnkeylinux/tracker/issues/) (used to report bugs and record feature requests) and the [Wiki](https://github.com/turnkeylinux/tracker/wiki) (used to propose and track appliance candidates and as a general purpose whiteboard for TKL development). 

Before opening a new issue, please check to see if a similar bug, issue or feature request already exists in the tracker. If a similar topic is currently open, post a comment stating that it also affects you. Knowing an issue affects multiple users is useful when we decide how to prioritize limited development resources. Please try and include any additional information you think might help us close the issue.

The ideal bug / issue report includes:
* A detailed description of the bug / issue
* Step by step instructions on how it may be reproduced
* the output that is generated from using the ``turnkey-version`` command, which should look like this:
```
turnkey-appliance_name-major_version.minor_version-debian_codename-architecture
```

The ideal feature request includes:
* A detailed description of the feature and the component it relates to
* One or more cases in which the feature might be of use
* Any other relevant information

Note that the tracker is not intended to for use as a forum for support or general discussion. For technical support or general discussion, please use the appropriate [forum](https://www.turnkeylinux.org/forum).
