'''
bisect_left

Runtime: 1201 ms, faster than 94.90% of Python3 online submissions for Successful Pairs of Spells and Potions.
Memory Usage: 37.5 MB, less than 27.20% of Python3 online submissions for Successful Pairs of Spells and Potions.
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
