#!/ bin/bash

# crontab for git
# if it detects some file or directories changed, it automatically fetch, merge, add, commit and push.

git_upate()
{
	git fetch --all
	git merge origin master
	git add .
	git commit -m "explore 2021"
	git push
}


check=`git status | grep "new file"`

if 

