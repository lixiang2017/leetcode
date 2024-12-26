'''
https://topaz.github.io/paste/#XQAAAQAVAgAAAAAAAAAzHIoib6p4r/McpYgEEgWhHoa5LSRMkVi92ASWXgRJn/53jpHpW/kJ3OghgKFv3WDrLT9Wp7oYNq2nPXyB+tAc8xVlAxmQJNlW1171NSfSVxOZdJER0R6iAZyTQkdrU18wiR3857L13eyldROWNihp69pGRHfBbpIYj65c6foaGwZfr2pK7mQQttE1fbh+DKGuU1gsNRCt45J7qga+kitCGPZfZaU0oXbxkBACLdXe+fSo8AwlVbSmaS+GIs3Wf/4qnhlkdEoDzZhakB3nA5bbN3aOYG2hzmN/wLwAwy/Jks8c0nuvh2NzW4UPaofpvdgBBhNWm8bIOmoVuI6NwWaHd9F5idnF5dRa4Hg+dgnOpPuIpvXLzR6TnPna23ACekq2m8MkZ5JOwiFW5sZ1RIlsWmWY2awFKhT8SiWd

https://www.reddit.com/r/adventofcode/comments/1hkgj5b/2024_day_23_solutions/?sort=confidence


u/4HbQ 
[LANGUAGE: Python] Code (12 lines)
Nice puzzle today. Here's my full solution without NetworkX.
First we construct a set of all computers and a set of all connections. For part 1, for all possible triples of computers, we check whether they are all connected, and at least one of them starts with the letter 't':
'''

from pathlib import Path
import os
from itertools import combinations

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")

# part1
computers, connections = set(), set()
for line in lines.split("\n"):
    a, b = line.strip().split("-")
    computers.update([a, b])
    connections.update([(a, b), (b, a)])

print(sum({(a, b), (b, c), (a, c)} < connections and "t" in (a+b+c)[::2] for a, b, c in combinations(computers, 3)))
# 1284

# part2
networks = [{c} for c in computers]
for n in networks:
    for c in computers:
        if all((c,d) in connections for d in n): n.add(c)

print(*sorted(max(networks, key=len)), sep=',')
# bv,cm,dk,em,gs,jv,ml,oy,qj,ri,uo,xk,yw