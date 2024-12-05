# Part2 I avoided sorting entirely.
import os 
from collections import Counter, defaultdict

ans = 0
ordering_rules = []
is_update_started = False


def is_update_in_right_order(update):
    n = len(update)
    for i in range(n - 1):
        for j in range(i + 1, n):
            r = f"{update[i]}|{update[j]}"
            if r not in ordering_rules:
                return False
    return True


def topological_sort(rules, update):
    # in degree
    in_d = Counter()
    graph = defaultdict(set)
    nodes_set = set(update)
    for rule in rules:
        # a -> b
        a, b = list(map(int, rule.split("|")))
        if a in nodes_set and b in nodes_set:
            in_d[a] = in_d[a]
            in_d[b] += 1
            graph[a].add(b)

    q = [x for x in in_d if in_d[x] == 0]
    sorted_update = []
    while q:
        x = q.pop(0)
        sorted_update.append(x)
        for child in graph[x]:
            in_d[child] -= 1
            if 0 == in_d[child]:
                q.append(child)
    return sorted_update

input_path_from_part1 = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'part1'), 'input')
with open(input_path_from_part1, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":
            is_update_started = True
        elif not is_update_started:
            ordering_rules.append(line)
        if is_update_started and line:
            update = list(map(int, line.split(",")))
            if not is_update_in_right_order(update):
                ans += topological_sort(ordering_rules, update)[len(update) // 2]


print('ans: ', ans) # ans:  4713