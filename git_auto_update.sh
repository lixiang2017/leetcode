#! /bin/bash

# crontab for git
# if it detects some file or directories changed, it automatically fetch, merge, add, commit and push.

git fetch --all
git merge orgin master

git_update() {
	git fetch --all
	git merge origin master
	git add .
	git commit -m "explore 2021"
	git push
}


# check=`git status | grep "new file"`

_git_is_dirty() {
	[ -n "$(git status -s)" ]
}

if _git_is_dirty; then
	git_update
fi

