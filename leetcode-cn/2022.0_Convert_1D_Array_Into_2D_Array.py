'''
1 -> 2, 2021 -> 2022. hello, 2022
执行用时：56 ms, 在所有 Python3 提交中击败了94.67% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了65.44% 的用户
通过测试用例：107 / 107
'''
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = []
        for r in range(m):
            ans.append(original[r * n: r * n + n])
        return ans 

'''
执行用时：48 ms, 在所有 Python3 提交中击败了99.86% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了50.14% 的用户
通过测试用例：107 / 107
'''
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        return [original[r * n: r * n + n] for r in range(m)]
        