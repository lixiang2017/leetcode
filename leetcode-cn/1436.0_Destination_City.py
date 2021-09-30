'''
Hash Table

执行用时：36 ms, 在所有 Python3 提交中击败了50.15% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了69.66% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a2b = {}
        for a, b in paths:
            a2b[a] = b
        city = paths[0][1]
        while city in a2b:
            city = a2b[city]
        return city

'''
Hash Set

执行用时：32 ms, 在所有 Python3 提交中击败了77.40% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.93% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        for s, _ in paths:
            starts.add(s)
        for _, e in paths:
            if e not in starts:
                return e

