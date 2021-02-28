#!/bin/bash

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt| xargs | tr -s  ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2" "$1}'

cat words.txt| xargs | tr -s  ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2,$1}'

cat words.txt| xargs -n1 | sort | uniq -c | sort -r | awk '{print $2,$1}'

# awk '{for(i=1;i<=NF;i++){array[$i]++;}};END{for(w in array){print w, array[w]}}' words.txt | sort -r -k2  # wrong answer

#
# 执行用时：0 ms, 在所有 Bash 提交中击败了100.00%的用户
# 内存消耗：3.7 MB, 在所有 Bash 提交中击败了89.51%的用户
awk '{for(i=1;i<=NF;i++){array[$i]++;}};END{for(w in array){print w, array[w]}}' words.txt | sort -rn -k2


# 
cat words.txt |
awk '{
    for(i = 1; i <= NF; i++){
        count[$i]++
    }
} END {
    for (k in count) {
        print k" "count[k]
    }
}' |
sort -rnk 2

# python commond line
python3 -c "a=open('words.txt').read().split();from collections import Counter;c=list(Counter(a).items());c.sort(key=lambda x:-x[1]);[print(x,y)for x,y in c]"


python3 -c "
a = open('words.txt').read().split()
from collections import Counter
c = list(Counter(a).items())
c.sort(key=lambda x: -x[1])
[print(x, y) for x, y in c]
"


python3 -c "
a = open('words.txt').read().split()
from collections import Counter
c = list(Counter(a).items())
c.sort(key=lambda x: -x[1])
for x, y in c:
    print(x, y)
"


: <<'END'
# result:
the 4
is 3
sunny 2
day 1
END
