import os 

path = os.path.join(os.path.dirname(__file__), "input")

pos = 0
with open(path) as f:
    for line in f:
        for i, ch in enumerate(line, start=1):
            if ch == "(":
                pos += 1
            elif ch == ")":
                pos -= 1
            if -1 == pos:
                print('pos ', i)
                break 

# pos  1795