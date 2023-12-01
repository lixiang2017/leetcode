import os 

path = os.path.join(os.path.dirname(__file__), "input")

ans = 0

with open(path) as f:
    for line in f:
        l, w, h = map(int, line.split("x"))
        a, b, _ = sorted([l, w, h])
        ans += 2 * (a + b) + l * w * h

print("ans ", ans) # 3737498