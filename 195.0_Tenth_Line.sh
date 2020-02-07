# Read from the file file.txt and output the tenth line to stdout.
awk '{if(NR==10)print $0}' file.txt

# Success
# Details 
# Runtime: 4 ms, faster than 73.14% of Bash online submissions for Tenth Line.
# Memory Usage: 3.6 MB, less than 100.00% of Bash online submissions for Tenth Line.