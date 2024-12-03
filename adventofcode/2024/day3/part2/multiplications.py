import os 
import re 

ans = 0
input_path_from_part1 = os.path.join(os.path.dirname(__file__), 'input1')
input_path_from_part1 = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'part1'), 'input')

do = True
with open(input_path_from_part1) as f:
    for line in f:
        # do = True # wrong here! There is relationship between lines@
        # mul or do or don't
        pat = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
        mul_do_not = re.findall(pat, line)
        # print(mul_do_not)
        for m in mul_do_not:
            if m == "do()":
                do = True
            elif m == "don't()":
                do = False
            else:
                if do:
                    match_object = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", m)
                    # print(match_object.group(1), match_object.group(2))
                    ans += int(match_object.group(1)) * int(match_object.group(2))

print('ans: ', ans) # ans:  89349241