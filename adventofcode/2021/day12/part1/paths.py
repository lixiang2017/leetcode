

from collections import defaultdict

def paths_count(file_name):

    graph = defaultdict(list)
    big = set()
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            u, v = line.split('-')
            graph[u].append(v)
            graph[v].append(u)
            for x in [u, v]:
                if x.isupper():
                    big.add(x)

    paths = set()
    def dfs(node, cur_path, seen_small):
        if node == 'end':
            paths.add(tuple(cur_path))
            return 

        for child in graph[node]:
            if child not in seen_small:
                dfs(child, cur_path + [child], 
                    seen_small | set([node if not node.isupper() else None])
                    )


    dfs('start', [], set())

    cnt = len(paths)
    print('cnt: ', cnt)
    return cnt 


c1 = paths_count('input1')
c2 = paths_count('input2')
c3 = paths_count('input3')
c = paths_count('input')

'''
cnt:  10
cnt:  19
cnt:  226
cnt:  5874
'''

