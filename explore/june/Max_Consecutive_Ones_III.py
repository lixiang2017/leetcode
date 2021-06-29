'''
approach: Two Pointers / Sliding Window
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 53.01 % of python3 submissions.
You are here!
Your memory usage beats 32.26 % of python3 submissions.
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = l = r = longest = 0
        N = len(nums)
        while l < N and r <= N:
            if zeros <= k:
                longest = max(longest, r - l)
                if r < N and nums[r] == 0:
                    zeros += 1
                r += 1
            else:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
        
        return longest
