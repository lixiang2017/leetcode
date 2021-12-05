
from collections import defaultdict, deque
import re 


# parents of every child color
ps = defaultdict(set)

with open('input') as f:
    for line in f:
        line = line.strip()
        if 'no other' in line:
            continue

        parent, children = line.split('contain')
        parent = parent.strip().replace('bags', '').replace('bag', '').strip()

        targets = re.findall(r'\d+ ([a-z ]+)[^bag]', children)      
        if targets:
            for t in targets:
                child = t.replace('bags', '').replace('bag', '').strip()
                ps[child].add(parent)


root = 'shiny gold'
q = deque(ps[root])
gold_parents = set(ps[root])
while q:
    node = q.popleft()
    for p in ps[node]:
        if p not in gold_parents:
            gold_parents.add(p)
            q.append(p)


print('gold_parents: ', len(gold_parents))

'''
('gold_parents: ', 355)
'''


