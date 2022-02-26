'''
寻找性质

执行用时：292 ms, 在所有 Python3 提交中击败了79.17% 的用户
内存消耗：43.1 MB, 在所有 Python3 提交中击败了50.00% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # graph
        g = defaultdict(set)
        for x, y in pairs:
            g[x].add(y)
            g[y].add(x)
        # find root
        root = next((node for node, neighbours in g.items() if len(neighbours) == len(g) - 1), -1)
        if -1 == root:
            return 0
        
        ans = 1
        for node, neighbours in g.items():
            if node == root:
                continue
            # to find parent
            parent = -1
            parent_size = maxsize
            curr_size = len(neighbours)
            for neighbour in neighbours:
                if curr_size <= len(g[neighbour]) < parent_size:
                    parent = neighbour
                    parent_size = len(g[neighbour])
            # is forest, cannot find parent or nodes set of parent is less than child
            if parent == -1 or any(parent != neighbour and neighbour not in g[parent] for neighbour in neighbours):
                return 0
            if parent_size == curr_size:
                ans = 2
        return ans 

