'''
approach: Mono Increasing Stack
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 67.86 % of python submissions.
You are here!
Your memory usage beats 63.93 % of python submissions.

ref:
https://leetcode.com/problems/find-the-most-competitive-subsequence/discuss/1027495/Python-Stack-solution-explained
'''

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        attempts = len(nums) - k
        stack = []
        for num in nums:
            while stack and stack[-1] > num and attempts:
                stack.pop()
                attempts -= 1
            stack.append(num)
        
        return stack[: k]
    