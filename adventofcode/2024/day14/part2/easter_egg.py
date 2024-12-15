from pathlib import Path
import os
import re


ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
groups = re.split("\n", lines)


def get_x_y(s):
    xy = s.strip().split("=")[1]
    x_str, y_str = xy.split(",")
    return int(x_str), int(y_str)

robots = []
for group in groups:
    # positions (p) and velocities (v)
    P, V = group.split()
    px, py = get_x_y(P)
    vx, vy = get_x_y(V)
    robots.append([px, py, vx, vy])

# wide, tall = 11, 7
wide, tall = 101, 103

seconds = 7371 

for t in range(seconds, seconds + 1):
    shape = [["*" for _ in range(wide)] for _ in range(tall)]
    print("+++++++ ", t, "+++++++++++++++")
    for px, py, vx, vy in robots:
        x = (px + vx * t) % wide
        y = (py + vy * t) % tall
        shape[y][x] = "1"
    
    # print shape
    for i in range(tall):
        print("".join([" " if ch != "1" else ch for ch in shape[i] ]))
    print()
    
    import time
    time.sleep(3)
    
# print('ans:', int(ans)) # 7371