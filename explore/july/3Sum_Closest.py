'''
Sort + Two Pointers
T:O(N^2)
S:O(1)

You are here!
Your runtime beats 90.58 % of python3 submissions.
You are here!
Your memory usage beats 98.11 % of python3 submissions.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = sum(nums[:3])
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, N - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(ans - target):
                    ans = total
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else: 
                    return target
        return ans
