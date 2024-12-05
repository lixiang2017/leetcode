import os 

ans = 0
ordering_rules = []
is_update_started = False


def is_update_in_right_order(update):
    # print(update)
    n = len(update)
    for i in range(n - 1):
        for j in range(i + 1, n):
            r = f"{update[i]}|{update[j]}"
            if r not in ordering_rules:
                return False
    return True

with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        line = line.strip()
        if line == "":
            is_update_started = True
        elif not is_update_started:
            ordering_rules.append(line)
        if is_update_started and line:
            update = list(map(int, line.split(",")))
            if is_update_in_right_order(update):
                ans += update[len(update) // 2]


print('ans: ', ans) # ans:  7307