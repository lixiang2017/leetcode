from pathlib import Path
import os
import re

'''
A: x a1 b1
B: y a2 b2
a1 * x + a2 * y = s
b1 * x + b2 * y = t
so,
x = (s * b2 - t * a2) / (a1 * b2 - a2 * b1)
y = (s * b1 - t * a1) / (a2 * b1 - a1 * b2)
'''


def get_x_y(s):
    x_part, y_part = s.strip().split(":")[1].split(",")
    # print(x_part.strip())
    # print(y_part.strip())
    if "+" in x_part:
        x_str = x_part.strip().split("+")[1]
    else:
        x_str = x_part.strip().split("=")[1]
    if "+" in y_part:
        y_str = y_part.strip().split("+")[1]
    else:
        y_str = y_part.strip().split("=")[1]
    return int(x_str), int(y_str)

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
groups = re.split("\n\n", lines)
for group in groups:
    print("++++++++++")
    # print(group)
    A, B, P = group.split("\n")
    a1, b1 = get_x_y(A)
    a2, b2 = get_x_y(B)
    s, t = get_x_y(P)
    s += 10000000000000
    t += 10000000000000
    div = a1 * b2 - a2 * b1
    if div == 0:
        continue
    x = (s * b2 - t * a2) / div
    y = (s * b1 - t * a1) / (-div)
    # if 0 <= x <= 100 and 0 <= y <= 100:
    x, y = int(x), int(y)
    if a1 * x + a2 * y == s and b1 * x + b2 * y == t:
        print("xy ", x, y)
        ans += 3 * x + y
    
print('ans:', int(ans)) # ans: 85644161121698