# Git Commands

A comprehensive guide to Git commands for version control. Use this document as a quick reference whenever you need to remember which command to use.

---

## Table of Contents
1. [Initial Setup](#initial-setup)
2. [Basic Commands](#basic-commands)
3. [Working with Branches](#working-with-branches)
4. [Committing Changes](#committing-changes)
5. [Remote Operations](#remote-operations)
6. [Undoing Changes](#undoing-changes)
7. [Viewing History](#viewing-history)
8. [Advanced Commands](#advanced-commands)
9. [Useful Workflows](#useful-workflows)

---

## Initial Setup

### Configure your Git identity
Before you start working, tell Git who you are:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Initialize a new repository
Create a Git repository in your current directory:

```bash
git init
```

### Clone a repository
Copy an existing repository from GitHub (or any remote) to your computer:

```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

---

## Basic Commands

### Check the status of your repository
See which files have been modified, staged, or are untracked:

```bash
git status
```

**Output example:**
- `modified:` - File has been changed but not staged
- `new file:` - File is new and untracked
- `deleted:` - File has been deleted

### Stage files for commit
**Option 1: Stage all changes**
```bash
git add .
```

**Option 2: Stage specific file**
```bash
git add path/to/file.txt
```

**Option 3: Stage all files of a specific type**
```bash
git add *.txt
```

**Option 4: Interactive staging (choose what to stage)**
```bash
git add -p
```
This lets you review each change and decide whether to stage it.

### View what's staged vs. unstaged

```bash
# See differences in unstaged files
git diff

# See differences in staged files
git diff --staged
# or
git diff --cached
```

---

## Committing Changes

### Create a commit
Save your staged changes with a message describing what you changed:

```bash
git commit -m "Your commit message here"
```

**Good commit message examples:**
- `"Add login validation"`
- `"Fix bug in user authentication"`
- `"Update documentation for API endpoints"`

### Commit all changes (skip staging)
Stage and commit all modified files in one command:

```bash
git commit -am "Your message"
```
⚠️ **Note:** This only works for modified files, not new untracked files.

### Write a detailed commit message
For longer messages, use an editor instead of `-m`:

```bash
git commit
```
This opens your default text editor. First line is the title, then blank line, then detailed description.

### Amend the last commit
Fix your last commit (change message or add forgotten files):

```bash
# Just change the message
git commit --amend -m "New message"

# Add forgotten file and keep the message
git add forgotten-file.txt
git commit --amend --no-edit
```

⚠️ **Warning:** Don't amend if you've already pushed to remote!

---

## Working with Branches

### List all branches
```bash
# Local branches only
git branch

# All branches (local + remote)
git branch -a
```

### Create a new branch
```bash
# Create branch (stay on current branch)
git branch branch-name

# Create and switch to new branch
git checkout -b branch-name
# or (newer syntax)
git switch -c branch-name
```

### Switch to a different branch
```bash
# Using checkout (old syntax)
git checkout branch-name

# Using switch (new syntax - recommended)
git switch branch-name
```

### Rename a branch
```bash
# Rename local branch you're on
git branch -m new-name

# Rename specific local branch
git branch -m old-name new-name
```

### Delete a branch
```bash
# Delete local branch (safe - prevents deleting unmerged branches)
git branch -d branch-name

# Force delete local branch
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name
```

### Create a branch from a remote branch
```bash
git checkout --track origin/remote-branch-name
# or
git checkout remote-branch-name
```

---

## Remote Operations

### View remote repositories
```bash
# List all remotes
git remote

# List remotes with URLs
git remote -v
```

### Add a remote repository
```bash
git remote add origin https://github.com/username/repo.git
```

### Push your commits to remote
```bash
# Push current branch to remote with same name
git push

# Push to specific remote and branch
git push origin branch-name

# Push all branches
git push --all origin

# Push and set upstream (links local to remote branch)
git push -u origin branch-name
```

### Pull changes from remote
Fetch and merge changes from remote in one command:

```bash
# Pull from current branch's tracked remote
git pull

# Pull from specific remote and branch
git pull origin branch-name
```

### Fetch changes (without merging)
Download changes from remote but don't merge them:

```bash
# Fetch from default remote
git fetch

# Fetch from specific remote
git fetch origin

# Fetch all remotes
git fetch --all
```

### Sync your branch with remote after rebase
```bash
git push --force-with-lease origin branch-name
```
⚠️ **Use with caution!** Only use if you've done a rebase or ammend locally.

---

## Undoing Changes

### Discard changes in working directory
```bash
# Discard changes in one file
git checkout -- path/to/file.txt

# Discard all changes
git checkout -- .
# or
git restore .
```

### Unstage files
Remove files from staging area (keep changes in working directory):

```bash
# Unstage all files
git reset

# Unstage specific file
git reset path/to/file.txt
```

### Undo last commit (keep changes)
```bash
git reset --soft HEAD~1
```
Changes go back to staging area. The commit is undone but your work is preserved.

### Undo last commit (discard changes)
```bash
git reset --hard HEAD~1
```
⚠️ **Dangerous!** This deletes your changes completely.

### Revert a commit (undo changes but keep history)
Create a new commit that undoes previous commit:

```bash
git revert commit-hash
```
This is safer than reset for shared branches because it keeps the history.

### Go back to a previous commit (check it out)
```bash
git checkout commit-hash
```
This puts you in "detached HEAD" state. You can look around but shouldn't make commits.

---

## Viewing History

### View commit history
```bash
# Simple list of commits
git log

# Show commits in one line (compact)
git log --oneline

# Show last 5 commits
git log -5

# Show commits with graph (visual branches)
git log --graph --oneline --all

# Show commits by specific author
git log --author="Author Name"

# Show commits with statistics (files changed, additions, deletions)
git log --stat
```

### Show specific commit details
```bash
# Show changes in a commit
git show commit-hash

# Show what changed in last commit
git show HEAD
```

### Search commit history
```bash
# Find commits with specific text in message
git log --grep="search text"

# Find commits that touched a specific file
git log -- path/to/file.txt
```

### Compare branches
```bash
# See difference between two branches
git diff branch1 branch2

# See commits in branch2 that are not in branch1
git log branch1..branch2
```

---

## Advanced Commands

### Merge branches
Combine changes from one branch into another:

```bash
# Switch to target branch first
git checkout main

# Merge source branch into current branch
git merge source-branch-name

# Merge with a message
git merge source-branch-name -m "Merge message"
```

### Rebase branches (replay commits on top of another branch)
Cleaner history than merge, but rewrites history:

```bash
# Rebase current branch onto another
git rebase target-branch

# Rebase and edit commits interactively
git rebase -i HEAD~5
```

This opens an editor where you can squash, reword, or reorder commits.

### Cherry-pick a commit
Copy a specific commit from one branch to another:

```bash
git checkout target-branch
git cherry-pick commit-hash
```

### Stash changes (temporary save)
Save your changes without committing them:

```bash
# Stash all changes
git stash

# Stash with a name/message
git stash save "description of what you're stashing"

# List all stashes
git stash list

# Apply last stash (keeps it in stash list)
git stash apply

# Apply and remove last stash
git stash pop

# Apply specific stash
git stash apply stash@{0}

# Delete a stash
git stash drop stash@{0}

# Delete all stashes
git stash clear
```

### Tag a commit
Mark important commits (usually for releases):

```bash
# Create a lightweight tag
git tag v1.0.0

# Create an annotated tag with message
git tag -a v1.0.0 -m "Version 1.0.0 release"

# Push tags to remote
git push origin v1.0.0

# Push all tags
git push origin --tags
```

### Blame (find who changed what)
See who made each change in a file:

```bash
git blame path/to/file.txt
```

### Interactive rebase (clean up commit history)
Edit previous commits before pushing:

```bash
# Edit last 3 commits
git rebase -i HEAD~3
```

Commands in the interactive editor:
- `pick` - use commit
- `reword` - use commit, edit message
- `squash` - use commit, combine with previous
- `fixup` - like squash but discard log message
- `drop` - remove commit

---

## Useful Workflows

### Typical workflow for feature development

```bash
# 1. Update main branch
git checkout main
git pull

# 2. Create feature branch
git checkout -b feature/my-feature

# 3. Make changes, commit them
git add .
git commit -m "Add my feature"

# 4. More changes
git add .
git commit -m "Fix feature bug"

# 5. Push to remote
git push -u origin feature/my-feature

# 6. Create Pull Request on GitHub website
# (then merge via GitHub UI)

# 7. Switch back to main and delete feature branch
git checkout main
git pull
git branch -d feature/my-feature
```

### Fixing mistakes in last commit

```bash
# Forgot to add a file
git add forgotten-file.txt
git commit --amend --no-edit

# Wrong commit message
git commit --amend -m "Correct message"
```

### Clean up local branches after deleted remotes

```bash
git remote prune origin
```

### See what would be deleted before hard reset

```bash
git clean -fd --dry-run
```

Then remove with:
```bash
git clean -fd
```

### Squash multiple commits into one

```bash
# Interactive rebase for last 3 commits
git rebase -i HEAD~3
```

In the editor:
- Keep first commit as `pick`
- Change others to `squash` or `fixup`
- Save and close editor

### Sync fork with upstream repository

```bash
# Add upstream if not already added
git remote add upstream https://github.com/original-owner/repo.git

# Fetch upstream changes
git fetch upstream

# Rebase your branch on upstream
git rebase upstream/main
```

### Create backup of local changes

```bash
# Save all uncommitted changes
git stash save "backup-$(date +%s)"

# List stashes to see your backups
git stash list
```

---

## Common Scenarios & Solutions

### I need to undo my last push
⚠️ **Only do this if no one else has pulled your changes!**

```bash
git reset --soft HEAD~1
git push --force-with-lease origin branch-name
```

### I accidentally committed to the wrong branch

```bash
# Copy the commit hash
git log

# Undo the commit on this branch
git reset --soft HEAD~1

# Switch to correct branch
git checkout correct-branch

# Commit there
git commit -m "your message"
```

### I have merge conflicts

```bash
# When pulling, conflicts appear
git status  # See conflicted files

# Edit files in your editor, resolve conflicts

# After fixing
git add resolved-file.txt
git commit -m "Resolve merge conflict"
```

### I want to see changes before committing

```bash
git diff  # See unstaged changes
git diff --staged  # See staged changes
git diff branch1 branch2  # Compare branches
```

---

## Tips & Best Practices

✅ **DO:**
- Write clear, descriptive commit messages
- Commit frequently with logical groupings
- Pull before you push
- Create branches for new features
- Review changes before committing

❌ **DON'T:**
- Commit directly to `main` branch
- Use `git push --force` (use `--force-with-lease` instead)
- Commit large binary files
- Leave uncommitted changes for days
- Amend commits that are already pushed

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Check status | `git status` |
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Create branch | `git checkout -b branch-name` |
| Switch branch | `git checkout branch-name` |
| Push to remote | `git push origin branch-name` |
| Pull from remote | `git pull` |
| View history | `git log --oneline` |
| Undo changes | `git checkout -- file.txt` |
| Undo commit | `git reset --soft HEAD~1` |
| Merge branch | `git merge branch-name` |
| Stash changes | `git stash` |
| Apply stash | `git stash pop` |

---

**Last updated:** 2026-05-03

