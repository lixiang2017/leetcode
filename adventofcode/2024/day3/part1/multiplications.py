import os 
import re 

ans = 0

with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        pat = r"mul\(\d{1,3},\d{1,3}\)"
        muls = re.findall(pat, line)
        # print(muls)
        for mul in muls:
            match_object = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", mul)
            # print(match_object.group(1), match_object.group(2))
            ans += int(match_object.group(1)) * int(match_object.group(2))

print('ans: ', ans) # ans:  159833790