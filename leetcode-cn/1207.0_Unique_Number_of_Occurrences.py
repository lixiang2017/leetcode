'''
执行用时：40 ms, 在所有 Python3 提交中击败了52.66% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了77.82% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        return len(c) == len(set(c.values()))
        