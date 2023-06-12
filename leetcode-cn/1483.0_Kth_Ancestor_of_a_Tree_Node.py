'''
binary lifting

执行用时：716 ms, 在所有 Python3 提交中击败了71.05% 的用户
内存消耗：48.6 MB, 在所有 Python3 提交中击败了73.68% 的用户
通过测试用例：16 / 16
'''
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent]
        for i in range(m):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa 

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                node = self.pa[node][i]
                if node < 0:
                    break 
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)


'''
执行用时：624 ms, 在所有 Python3 提交中击败了80.26% 的用户
内存消耗：48.1 MB, 在所有 Python3 提交中击败了92.11% 的用户
通过测试用例：16 / 16
'''
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent]
        for i in range(m):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa 

    def getKthAncestor(self, node: int, k: int) -> int:
        while k and node != -1:
            lb = k & -k 
            node = self.pa[node][lb.bit_length() - 1]
            k ^= lb 
        return node 

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)


'''
执行用时：716 ms, 在所有 Python3 提交中击败了71.05% 的用户
内存消耗：48.5 MB, 在所有 Python3 提交中击败了80.26% 的用户
通过测试用例：16 / 16
'''
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent]
        for i in range(m):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa 

    def getKthAncestor(self, node: int, k: int) -> int:
        while k and ~node:
            lb = k & -k 
            node = self.pa[node][lb.bit_length() - 1]
            k ^= lb 
        return node 

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
