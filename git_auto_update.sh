#! /bin/bash

# crontab for git
# if it detects some file or directories changed, it automatically fetch, merge, add, commit and push.

git fetch --all
git merge origin master

git_update() {
	git fetch --all
	git merge origin master
	git add .
	today=$(date "+%Y-%m-%d %H:%M:%S")
	commit_msg="[update](${today}): auto commit and push"
	echo $commit_msg
	git commit -m "${commit_msg}"
	# git commit -m "explore 2022"
	git push origin master
	echo "update and push code success"
}


# check=`git status | grep "new file"`

_git_is_dirty() {
	[ -n "$(git status -s)" ]
}

if _git_is_dirty; then
	git_update
fi

