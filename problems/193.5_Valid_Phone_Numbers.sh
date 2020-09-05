# Read from the file file.txt and output all valid phone numbers to stdout.
# using egrep
egrep '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt

# Success
# Details 
# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 50.00% of Bash online submissions for Valid Phone Numbers.