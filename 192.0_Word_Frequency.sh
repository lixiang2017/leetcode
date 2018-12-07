# Read from the file words.txt and output the word frequency list to stdout.
#! /bin/bash
cat words.txt | tr -cs "[a-z][A-Z]" "\n" | tr A-Z a-z | sort | uniq -c | awk '{print $2, $1}' | sort -k 2nr