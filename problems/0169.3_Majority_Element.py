'''
摩尔投票法
T: O(N)
S: O(1)

Runtime: 191 ms, faster than 63.67% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 43.74% of Python3 online submissions for Majority Element.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = float('inf')
        cnt = 0
        for x in nums:
            if x == major:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                major = x
                cnt = 1
                
        return major
