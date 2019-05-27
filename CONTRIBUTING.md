# Contributor's Guide

Anyone with a GitHub account can propose changes to files in this repository. This document describes instructions and best practices for contributing to this repository. If you are a student unfamiliar with Git and GitHub, please consult the [official Git guides](https://guides.github.com/) or the [professor's Git notes](/notes/clis/git.md), or ask the professor for a crash course.

## Step 1: Fork the Repository

First, "fork" the course repository via the GitHub.com online interface to create a copy under the ownership of your own GitHub user. After doing so, you should be able to view your fork online at `https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-201905`.

Next, use GitHub Desktop (or Git Bash, see commands below) to "clone", or download, your fork onto your computer:

```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-201905.git # this is the HTTPS address, but alternatively you can use the SSH address
cd nyu-info-2335-201905
```

By cloning, you should see a remote address called "origin" has already been established between your local repository and your forked remote repository:

```sh
git remote -v
#> origin	https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-201905.git (fetch)
#> origin	https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-201905.git (push)
```

If you cloned the repo using GitHub Desktop, you may see both an "origin" and an "upstream" address after running that last `git remote -v` command, in which case there is no need to configure the "upstream" remote address manually.

Otherwise, you'll need to manually establish a relationship between your local repository and the "upstream" remote repository, which will allow you to keep your fork up-to-date:

```sh
git remote add upstream https://github.com/prof-rossetti/nyu-info-2335-201905.git # this is the HTTPS address, but alternatively you can use the SSH address

git remote -v
#> origin	https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-201905.git (fetch)
#> origin	https://github.com/YOUR_GITHUB_USERNAME/nyu-info-2335-201905.git (push)
#> upstream	https://github.com/prof-rossetti/nyu-info-2335-201905.git (fetch)
#> upstream	https://github.com/prof-rossetti/nyu-info-2335-201905.git (push)
```

### Refreshing your Fork

If you have previously forked the course repository and now your fork is out of date / behind the "upstream" course repository, then follow these steps to **refresh your fork** from the command-line (Terminal or Git Bash):

```sh
git branch # make sure you are on the "master" branch

git pull upstream master # update your local repository to reflect the contents of the "upstream" remote repository

git push origin master # update your "origin" remote repository to reflect the contents of your local repository
```

> NOTE: after fetching, if you see conflicts when you pull or push, run: `git reset --hard upstream master` to do a hard reset.

> WARNING: refreshing your fork will delete any previous changes you have committed there that aren't reflected in the "upstream" course repository. So make sure any outstanding Pull Requests have been merged before refreshing your fork!


## Step 2: Revise File Contents

To revise content, navigate to a file in your forked repository via the GitHub.com online interface, then click the "pencil" icon to reveal an online text editor. When done editing a file, "commit" to save the changes. After doing so, you should be able to view your changes reflected online in your own fork.

> NOTE: Most files in this repository are written in a syntax called Markdown. For reference, see this [Markdown Cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf).

## Step 3: Submit a Pull Request

After your fork contains the changes you'd like to be included in the course repository, navigate to the original course repository and create a Pull Request (PR) using the GitHub.com online interface. In the PR message, describe what changes you made and why.

An instructor should review your PR within a timely manner. If the instructor accepts your changes, the instructor will merge them into the course repository's master branch, at which point you should be able to view your changes reflected in the course repository. Else if there are issues with the submission, the instructor should provide further instruction by commenting on the PR, and may close it.

Congratulations! :clap: Thanks! :pray:
