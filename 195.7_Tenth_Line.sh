# Read from the file file.txt and output the tenth line to stdout.
sed -n 10p file.txt

# Success
# Details 
# Runtime: 4 ms, faster than 73.14% of Bash online submissions for Tenth Line.
# Memory Usage: 3.7 MB, less than 95.24% of Bash online submissions for Tenth Line.

# explain
# sed [option] [command] file(s)
# sed [option] -f scriptfile file(s)
# -n, --quiet, --silent
# 10, the 10th line
# p, print/ s, substitue/ d, delete  # like vim
