# Read from the file file.txt and output all valid phone numbers to stdout.
# using sed
sed -n -r '/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/p' file.txt

# Success
# Details 
# Runtime: 8 ms, faster than 24.17% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 57.14% of Bash online submissions for Valid Phone Numbers.

# explain
# -n, --quiet, --silent
# -r, --regexp-extended
# ^    start
# $    end
