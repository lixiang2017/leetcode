#! /bin/bash
 
# examle
# mv 989.3_Add_to_Array-Form_of_Integer.py 0989.3_Add_to_Array-Form_of_Integer.py
# why
# more than 1000 problems

# for file in `ls *.py` # not complete
for file in `ls |grep -vE  'count|rename'`
do
        echo 'before rename:', $file
        # echo $file | awk -F . '{print $1}' # also work
        # echo $file | cut -f1 -d"." # also work
        problem_no="$(awk -F . '{print $1}' <<< $file)"
        echo problem_no, $problem_no
        if [ ${#problem_no} -lt 4 ];
        then
                new_file=0$file
                echo 'after rename', $new_file
                mv $file $new_file
        fi

done
