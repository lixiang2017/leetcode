'''
执行用时：220 ms, 在所有 Python3 提交中击败了89.11% 的用户
内存消耗：35.1 MB, 在所有 Python3 提交中击败了53.47% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)
        ans = [0] * n
        potions.sort()
        for i, s in enumerate(spells):
            least = (success + s - 1) // s
            idx = bisect_left(potions, least)
            ans[i] = m - idx        
        return ans 
        