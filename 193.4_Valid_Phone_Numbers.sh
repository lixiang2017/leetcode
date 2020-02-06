# Read from the file file.txt and output all valid phone numbers to stdout.
# using awk, using [[:digit:]]
awk '/^([[:digit:]]{3}-|\([[:digit:]]{3}\) )[[:digit:]]{3}-[[:digit:]]{4}$/' file.txt

# Success
# Details 
# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.4 MB, less than 7.14% of Bash online submissions for Valid Phone Numbers.