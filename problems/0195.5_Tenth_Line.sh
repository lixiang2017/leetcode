# Read from the file file.txt and output the tenth line to stdout.
awk 'FNR == 10 {print; exit}'  file.txt

# Success
# Details 
# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Tenth Line.
# Memory Usage: 3.7 MB, less than 76.19% of Bash online submissions for Tenth Line.