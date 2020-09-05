# Read from the file file.txt and output the tenth line to stdout.
# using while
cnt=0
while read line && [ $cnt -le 10 ]; do
	let 'cnt = cnt + 1'
	if [ $cnt -eq 10 ]; then
		echo $line
		exit 0
	fi
done < file.txt

# Success
# Details 
# Runtime: 4 ms, faster than 73.14% of Bash online submissions for Tenth Line.
# Memory Usage: 3.7 MB, less than 57.14% of Bash online submissions for Tenth Line.