# Project 0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it. `status` has a sample of what a well done filled in entry looks like.

Entries that are currently crossed out we will get to later in the course that you could go back and write some details on later.

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Used to make a clone of an existing repository in a new directory.
  - `git clone [url]`
- add
  - Add one or more files to staging.
  - `git add [file]`
- rm
  - Remove one or more files from staging.
  - `git remove [file]`
- commit
  - Used to save your changes to the local repository if they have been added (`git add`). You can include modified files with `-a`.
  - `git commit -a`
- push
  - Updates the remote branch with the local commits.
  - `git push`
- fetch
  - Used to download commits, files, and references from a remote repository.
  - `git fetch`
- merge
  - Used to integrate changes from another branch.
  - `git merge`
- pull
  - Used to fetch and download content from a remote repository and immediately update the local repository to match that content.
  - `git pull`
- branch
  - Allows you to create, list, rename, and delete branches.
  - `git branch`
- checkout
  - Lets you navigate between the branches created by git branch.
  - `git checkout`
- ~~init~~
  - Creates an empty Git repository.
  - `git init`
- ~~remote~~
  - Lets you create, view, and delete connections to other repositories.
  - `git remote`

## git files & folders

- .git folder
  - Contains all information that is necessary for the project and all information relating commits, remote repository address, etc. It also contains a log that stores the commit history. This log can help you to roll back to the desired version of the code.
- .gitignore file
  - A text file that tells Git which files or folders to ignore in a project.
- ~~.git/hooks~~
  - Ordinary scripts that Git executes when certain events occur in the repository.

## GitHub

- Pull requests
  - An event in Git where a contributor asks a maintainer of a Git repository to review code they want to merge into a project.
- SSH authentication to repositories
  - Makes all your traffic encrypted. You are authenticated using your own set of SSH keys.
- ~~Actions~~

## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)

## Submission

1. Commit and push your changes to your repository. Verify that these changes show in your course repository, https://github.com/WSU-kduncan/ceg3120-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder. Sample link: https://github.com/WSU-kduncan/ceg3120-YOURGITHUBUSERNAME/blob/main/Projects/Project0