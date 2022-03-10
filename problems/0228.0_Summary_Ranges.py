'''
T: O(N)
S: O(1)

Runtime: 50 ms, faster than 31.39% of Python3 online submissions for Summary Ranges.
Memory Usage: 13.9 MB, less than 88.25% of Python3 online submissions for Summary Ranges.
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        
        ans = []
        # 避免最后一步讨论
        first = nums[0]
        nums.append(first)
        prev_idx = 0
        for i, x in enumerate(nums):
            if i - prev_idx == x - nums[prev_idx]:
                continue
            else:
                if i - 1 == prev_idx:
                    ans.append(str(nums[i - 1]))
                else:
                    ans.append(str(nums[prev_idx]) + '->' + str(nums[i - 1]))
                prev_idx = i
        
        return ans