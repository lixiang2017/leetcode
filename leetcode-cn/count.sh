#! /bin/bash
# count the problem number include solved and attempted
ls | grep -E '^[0-9]' | awk '{print substr($1, 1, 4)}' | uniq | wc -l
