'''
sort + two pointers

Runtime: 6989 ms, faster than 50.41% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.2 MB, less than 12.36% of Python3 online submissions for 3Sum Closest.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = sum(nums[: 3]), len(nums)
        for i, x in enumerate(nums):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(ans - target):
                    ans = s 
                if s < target:
                    j += 1
                else:
                    k -= 1
        return ans 



'''
Runtime: 8912 ms, faster than 16.42% of Python3 online submissions for 3Sum Closest.
Memory Usage: 14.2 MB, less than 53.95% of Python3 online submissions for 3Sum Closest.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, n = sum(nums[: 3]), len(nums)
        for i, x in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k < n - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(ans - target):
                    ans = s 
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    return target
        return ans 

