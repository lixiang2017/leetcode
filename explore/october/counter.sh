#! /bin/bash
# to count solved problems in current month
ls *.py  | awk -F '.' '{print $1}' | sort  | uniq  |wc -l
