# Read from the file file.txt and output the tenth line to stdout.
awk 'FNR == 10 {print }'  file.txt

# Success
# Details 
# Runtime: 4 ms, faster than 73.14% of Bash online submissions for Tenth Line.
# Memory Usage: 3.7 MB, less than 95.24% of Bash online submissions for Tenth Line.
