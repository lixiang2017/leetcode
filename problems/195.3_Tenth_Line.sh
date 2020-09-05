# Read from the file file.txt and output the tenth line to stdout.
if [ `cat file.txt | wc -l` -lt 10 ]
	then echo ''
else
	head -10 file.txt | tail -1
fi

# Success
# Details 
# Runtime: 4 ms, faster than 73.14% of Bash online submissions for Tenth Line.
# Memory Usage: 3.9 MB, less than 9.52% of Bash online submissions for Tenth Line.
