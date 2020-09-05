# Read from the file file.txt and output all valid phone numbers to stdout.
# using sed, using [[:digit:]]
sed -n -r  '/^(\([[:digit:]]{3}\) |[[:digit:]]{3}-)[[:digit:]]{3}-[[:digit:]]{4}$/p' file.txt

# Success
# Details 
# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 96.43% of Bash online submissions for Valid Phone Numbers.