import os 

path = os.path.join(os.path.dirname(__file__), "input")

ans = 0
with open(path) as f:
    for line in f:
        for ch in line:
            if ch == "(":
                ans += 1
            elif ch == ")":
                ans -= 1

print('ans ', ans) # ans  74