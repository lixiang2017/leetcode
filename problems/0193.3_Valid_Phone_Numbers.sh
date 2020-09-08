# Read from the file file.txt and output all valid phone numbers to stdout.
# using awk
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

# Success
# Details 
# Runtime: 4 ms, faster than 56.50% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.4 MB, less than 7.14% of Bash online submissions for Valid Phone Numbers.