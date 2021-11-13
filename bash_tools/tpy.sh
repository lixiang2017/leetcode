#! /bin/bash

# quick touch a python file with a given question name from leetcode


# Define a function here
# touch a python file from explore part of leetcode
# example:
#	texpy Find the Smallest Divisor Given a Threshold    

texpy () {
	echo 'touch a python file here'
	echo 'the number of arguments is ' $#
	echo 'all parameters are ' $@
	# for ARG in "$@";
	# do
	# 	echo 'arg: ' $ARG
	# done
	# arguments=("$@")
	# echo 'the last argument is ', "${@:-1}"   # not work
	# echo 'the last arguemnt is ', $BASH_ARGV
	# file_name="'${arguments[@]}'"
	# file_name="'${arguments[: -1]}'"  # wrong
	old="$IFS"
	IFS='_'
	# file_name="'$*'"
	file_name="$*"
	IFS=$old
	file_name+=.py
	echo 'filename: ' $file_name
	touch $file_name
	echo 'touch a python file ' $file_name 'done.'
	# open the file with sublime text
	st $file_name
}



# touch a python file from problems part of leetcode
# example:
#	tprpy 4. Median of Two Sorted Arrays
#	tprpy 56. Merge Intervals   
#	tprpy 345. Reverse Vowels of a String  
#	tprpy 942. DI String Match
#	tprpy 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

tprpy () {
        echo 'touch a python file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@
        # for ARG in "$@";
        # do
        #         echo 'arg: ' $ARG
        # done
        # arguments=("$@")
        # echo 'the last argument is ', "${@:-1}"   # not work
        # echo 'the last arguemnt is ', $BASH_ARGV
        # file_name="'${arguments[@]}'"
        # file_name="'${arguments[: -1]}'"  # wrong

        # old="$IFS"
        # IFS='_'
        # file_name="'$*'"
        # file_name="$*"
        # IFS=$old

	# filename = 0(depend on len of $1) + $1 + [0-9]_ + other arguments + .py
	problem_no=$1
	# problem_no_len=`expr length "$problem_no"` # not work on macOS  # expr: syntax error
    # problem_no_len=$(echo -n $problem_no | wc -c)
    # problem_no_len=$(printf $problem_no | wc -c)
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
	case ${problem_no_len} in
		2)
			problem_no=000$problem_no
			;;
		3)
			problem_no=00$problem_no
			;;
		4|'4')
			problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
			;;
        *)
            echo 'Invalid length'
            ;;
	esac
	problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

	problem_name=''
	position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
		if [ $position -gt 1 ]; then
			problem_name+=_${ARG}
		fi
		position+=1
        done


	file_name=${problem_no}${problem_name}

        file_name+=.py
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a python file ' $file_name 'done.'
	# open the file with sublime text
	st $file_name
}



# touch a cpp file for explore
texcpp () {
    echo 'touch a cpp file here'
    echo 'the number of arguments is ' $#
    echo 'all parameters are ' $@
    old="$IFS"
    IFS='_'
    file_name="$*"
    IFS=$old
    file_name+=.cpp
    echo 'filename: ' $file_name
    touch $file_name
    echo 'touch a cpp file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}

# touch a cpp file for problems
tprcpp () {
        echo 'touch a cpp file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.cpp
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a cpp file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}



# touch a c file for problems
tprc () {
        echo 'touch a c file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.c
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a c file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}





# touch a Java file for explore
texjava () {
    echo 'touch a Java file here'
    echo 'the number of arguments is ' $#
    echo 'all parameters are ' $@
    old="$IFS"
    IFS='_'
    file_name="$*"
    IFS=$old
    file_name+=.java
    echo 'filename: ' $file_name
    touch $file_name
    echo 'touch a Java file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}

# touch a Java file for problems
tprjava () {
        echo 'touch a Java file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.java
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a Java file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}



# add language golang
# touch a Go file for explore
texgo () {
    echo 'touch a Go file here'
    echo 'the number of arguments is ' $#
    echo 'all parameters are ' $@
    old="$IFS"
    IFS='_'
    file_name="$*"
    IFS=$old
    file_name+=.go
    echo 'filename: ' $file_name
    touch $file_name
    echo 'touch a Go file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}

# touch a Go file for problems
tprgo () {
        echo 'touch a Go file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.go
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a Go file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}


# add language JavaScript
# touch a js file for explore
texjs () {
    echo 'touch a js file here'
    echo 'the number of arguments is ' $#
    echo 'all parameters are ' $@
    old="$IFS"
    IFS='_'
    file_name="$*"
    IFS=$old
    file_name+=.js
    echo 'filename: ' $file_name
    touch $file_name
    echo 'touch a js file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}

# touch a js file for problems
tprjs () {
        echo 'touch a js file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.js
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a js file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}




# touch a sql file for problems
tprsql () {
        echo 'touch a sql file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.sql
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a sql file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}



# touch a c sharp file for problems
tprcs () {
        echo 'touch a c sharp file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.cs
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a c sharp file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}



texsql () {
    echo 'touch a sql file here'
    echo 'the number of arguments is ' $#
    echo 'all parameters are ' $@
    # for ARG in "$@";
    # do
    #   echo 'arg: ' $ARG
    # done
    # arguments=("$@")
    # echo 'the last argument is ', "${@:-1}"   # not work
    # echo 'the last arguemnt is ', $BASH_ARGV
    # file_name="'${arguments[@]}'"
    # file_name="'${arguments[: -1]}'"  # wrong
    old="$IFS"
    IFS='_'
    # file_name="'$*'"
    file_name="$*"
    IFS=$old
    file_name+=.sql
    echo 'filename: ' $file_name
    touch $file_name
    echo 'touch a sql file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}


# rust
# touch a rust file for problems
tprrust () {
        echo 'touch a rust file here'
        echo 'the number of arguments is ' $#
        echo 'all parameters are ' $@

    problem_no=$1
    problem_no_len=${#problem_no}
    echo 'problem_no_len: ', $problem_no_len
    case ${problem_no_len} in
        2)
            problem_no=000$problem_no
            ;;
        3)
            problem_no=00$problem_no
            ;;
        4|'4')
            problem_no=0$problem_no
            echo 'problem_no_length is four, problem_no: ', $problem_no
            ;;
        *)
            echo 'Invalid length'
            ;;
    esac
    problem_no=${problem_no}0
    echo 'problem_no after normal: ', $problem_no

    problem_name=''
    position=1
        for ARG in "$@";
        do
                echo 'arg: ' $ARG
        if [ $position -gt 1 ]; then
            problem_name+=_${ARG}
        fi
        position+=1
        done

    file_name=${problem_no}${problem_name}

        file_name+=.rs
        echo 'filename: ' $file_name
        touch $file_name
        echo 'touch a rust file ' $file_name 'done.'
    # open the file with sublime text
    st $file_name
}