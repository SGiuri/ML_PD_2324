
# Git Cheatsheet

This cheatsheet provides basic commands and examples for using Git.

## Git Configuration

Set up your Git identity:
```
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
```

Check your configuration:
```
git config --list
```

## Creating Repositories

Start a new repository or get one from an existing URL:
```
git init [project-name]
git clone [url]
```

## Basic Snapshotting

Check the status of your files:
```
git status
```

Add a file to the staging area:
```
git add [file]
```

Commit your staged content as a new commit snapshot:
```
git commit -m "[descriptive message]"
```

## Branching and Merging

List your branches:
```
git branch
```

Create a new branch:
```
git branch [branch-name]
```

Switch to another branch:
```
git checkout [branch-name]
```

Merge a branch into your current branch:
```
git merge [branch]
```

## Sharing and Updating Projects

Add a remote repository:
```
git remote add [shortname] [url]
```

Fetch from and integrate with another repository or a local branch:
```
git fetch [remote]
git pull [remote] [branch]
```

Push your branch to a remote repository:
```
git push [remote] [branch]
```

## Inspection and Comparison

Inspect the working directory and staging area:
```
git status
```

Show the commit history:
```
git log
```

Show changes between commits, commit and working tree, etc:
```
git diff
```
