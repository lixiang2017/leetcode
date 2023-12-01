import os 

path = os.path.join(os.path.dirname(__file__), "input")

ans = 0

with open(path) as f:
    for line in f:
        l, w, h = map(int, line.split("x"))
        ans += 2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l)

print("ans ", ans) # 1586300