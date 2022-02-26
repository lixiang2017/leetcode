'''
执行用时：184 ms, 在所有 Python3 提交中击败了6.09% 的用户
内存消耗：40.6 MB, 在所有 Python3 提交中击败了19.23% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        x = 0
        c = Counter()
        for u, v in edges:
            c[u] += 1
            c[v] += 1
            if c[u] == n - 1:
                x = u
            if c[v] == n - 1:
                x = v
        return x


'''
执行用时：192 ms, 在所有 Python3 提交中击败了6.09% 的用户
内存消耗：40.8 MB, 在所有 Python3 提交中击败了14.10% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        c = Counter()
        for u, v in edges:
            c[u] += 1
            c[v] += 1
        # last one
        u, v = edges[-1]
        return [node for node in [u, v] if c[node] == n - 1][0]
        