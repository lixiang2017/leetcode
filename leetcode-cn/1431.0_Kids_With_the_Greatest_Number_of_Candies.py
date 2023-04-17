'''
执行用时：44 ms, 在所有 Python3 提交中击败了19.52% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了22.52% 的用户
通过测试用例：103 / 103
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return [x + extraCandies >= m for x in candies]
        
        