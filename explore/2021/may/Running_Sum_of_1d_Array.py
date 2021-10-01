'''
approach: DP / Prefix Sum
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 61.92 % of python3 submissions.
You are here!
Your memory usage beats 43.79 % of python3 submissions.
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total, running = 0, []
        for num in nums:
            total += num
            running.append(total)
        return running



'''
approach: DP / Prefix Sum
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 61.92 % of python3 submissions.
You are here!
Your memory usage beats 98.00 % of python3 submissions.
'''

from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
        

'''
approach: DP / Prefix Sum
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 84.39 % of python3 submissions.
You are here!
Your memory usage beats 43.79 % of python3 submissions.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
