#! /bin/bash
# count leetcode.com and leetcode-cn.com, stored files at localhost.
# include accpeted and attempted, the attempted will be a very small number.
# not include `explore` topic in leetcode.com, so the result will less than real sum of accepted number in both websites.
# not include `shell`/`lcp`/`sword2offer`/`CrackingTheCodingInterview` in leetcode-cn.com

echo 'leetcode.com and leetcode-cn.com problems count: '
ls problems leetcode-cn |  grep -E '^[0-9]' | awk '{print substr($1, 1, 4)}' | uniq |wc -l

echo 'leetcode.com problems count: '
ls problems |  grep -E '^[0-9]' | awk '{print substr($1, 1, 4)}' | uniq |wc -l

echo 'leetcode-cn.com problems count: '
ls leetcode-cn |  grep -E '^[0-9]' | awk '{print substr($1, 1, 4)}' | uniq |wc -l

echo 'database count: '
ls leetcode-cn/sql |  grep -E '^[0-9]' | awk '{print substr($1, 1, 4)}' | uniq |wc -l
