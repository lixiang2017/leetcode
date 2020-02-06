# Read from the file file.txt and output all valid phone numbers to stdout.
# using grep
grep -P '^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$' file.txt

# Success
# Details 
# Runtime: 8 ms, faster than 24.17% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 96.43% of Bash online submissions for Valid Phone Numbers.

# explain
# -P, --perl-regexp
# ^    start
# $    end
# \d    digit
# |    or