

from collections import defaultdict

def paths_count(file_name):

    graph = defaultdict(list)
    big = set()
    small = set()
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            u, v = line.split('-')
            graph[u].append(v)
            graph[v].append(u)
            for x in [u, v]:
                if x.isupper():
                    big.add(x)
                if x.islower() and x not in ['start', 'end']:
                    small.add(x)

    paths = set()
    def dfs(node, cur_path, seen_small):
        print('cur_path: ', cur_path)
        if node == 'end':
            paths.add(tuple(cur_path))
            return 

        for child in graph[node]:
            if (child in big or (seen_small[child] <= 1)) and child != 'start':
                if child in small:
                    seen_small[child] += 1
                dfs(child, cur_path + [child], seen_small)
                if child in small:
                    seen_small[child] -= 1

    seen_small_cnt = defaultdict(int)
    dfs('start', [], seen_small_cnt)

    cnt = len(paths)
    print(paths)
    print('cnt: ', cnt)
    return cnt 


c1 = paths_count('input1')
# c2 = paths_count('input2')
# c3 = paths_count('input3')
# c = paths_count('input')

'''
wrong, all small cave can be visited twice.
'''

