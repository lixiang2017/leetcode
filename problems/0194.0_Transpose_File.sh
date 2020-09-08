# Read from the file file.txt and print its transposed content to stdout.
awk '{
	for(i=1; i<=NF; i++) {
		if(NR==1)
			{matrix[i] = $i;}
		else
			{matrix[i] = matrix[i] " " $i;}
	}
}

END {
	for (i in matrix) {
		print matrix[i]
	}
}' file.txt

# Success
# Details 
# Runtime: 8 ms, faster than 77.16% of Bash online submissions for Transpose File.
# Memory Usage: 3.7 MB, less than 25.00% of Bash online submissions for Transpose File.

# explain
# NF: Number of Fields
# NR: Number of Records
