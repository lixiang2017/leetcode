'''
Hint 1: Find the minimum prefix sum.

Time: O(N)
Space: O(1)

Success
Details 
Runtime: 16 ms, faster than 85.56% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
Memory Usage: 13.2 MB, less than 92.78% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
'''


class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefixSum = 0
        minPrefixSum = sys.maxint
        
        for num in nums:
            prefixSum += num
            minPrefixSum = min(minPrefixSum, prefixSum)
        
        return 1 if minPrefixSum >= 0 else - minPrefixSum + 1



'''
prefix sum

Time: O(N)
Space: O(1)

Runtime: 28 ms, faster than 90.75% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
Memory Usage: 14.3 MB, less than 44.63% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre = 0
        ans = 1
        for x in nums:
            pre += x
            ans = max(ans, -pre + 1)
        return ans
