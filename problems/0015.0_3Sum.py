'''
sort + two pointers

Runtime: 1608 ms, faster than 36.99% of Python3 online submissions for 3Sum.
Memory Usage: 17.4 MB, less than 74.21% of Python3 online submissions for 3Sum.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue         
            l, r = i + 1, N - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if r < N - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                elif t > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans
