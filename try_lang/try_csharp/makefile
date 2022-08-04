
# make run file=hello
run:
	mcs $(file).cs && mono $(file).exe


# make run1 file=hello.cs
run1:
	mcs $(file)
	mono $(file:.cs=.exe)


clean:
	rm -rf *.exe 