'''
approach: Two Pointers + Hash Set
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 31.24 % of python3 submissions.
You are here!
Your memory usage beats 44.42 % of python3 submissions.
'''


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maximum = 0
        N = len(nums)
        l = r = 0
        seen = set()
        current_total = 0
        while l < N and r < N:
            while r < N and nums[r] not in seen:
                seen.add(nums[r])
                current_total += nums[r]
                maximum = max(maximum, current_total)
                r += 1
            if r == N:
                break
            while l < N and nums[r] in seen:
                seen.remove(nums[l])
                current_total -= nums[l]
                l += 1
                
        return maximum
        