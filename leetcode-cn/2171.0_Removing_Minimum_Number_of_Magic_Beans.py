'''
执行用时：308 ms, 在所有 Python3 提交中击败了83.11% 的用户
内存消耗：26.3 MB, 在所有 Python3 提交中击败了62.25% 的用户
通过测试用例：64 / 64
'''

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        taken = 0
        for i, b in enumerate(beans):
            taken = max(taken, b * (n - i))
        return sum(beans) - taken  
