from pathlib import Path
import os
import re
from collections import Counter

# wide, tall = 11, 7
wide, tall = 101, 103

seconds = 100
cnt = Counter()

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
groups = re.split("\n", lines)


def get_x_y(s):
    xy = s.strip().split("=")[1]
    x_str, y_str = xy.split(",")
    return int(x_str), int(y_str)

for group in groups:
    # positions (p) and velocities (v)
    P, V = group.split()
    px, py = get_x_y(P)
    vx, vy = get_x_y(V)
    x = (px + vx * 100) % wide
    y = (py + vy * 100) % tall
    cnt[(x, y)] += 1


def safety_factor():
    mid_x = wide // 2
    mid_y = tall // 2
    # each quadrant, f1, f2, f3, f4
    f1 = f2 = f3 = f4 = 0
    for (x, y), c in cnt.items():
        if x < mid_x and y < mid_y:
            f1 += c
        elif x > mid_x and y < mid_y:
            f2 += c
        elif x < mid_x and y > mid_y:
            f3 += c
        elif x > mid_x and y > mid_y:
            f4 += c 

    print(cnt)
    print(f1, f2, f3, f4)
    return f1 * f2 * f3 * f4

ans = safety_factor()
print('ans:', int(ans)) # ans: 225552000