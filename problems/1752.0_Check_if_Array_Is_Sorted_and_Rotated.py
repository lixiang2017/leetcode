'''
approach: One Pass
Time: O(N)
Space: O(1)

Runtime: 36 ms, faster than 51.72% of Python3 online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 14.1 MB, less than 91.82% of Python3 online submissions for Check if Array Is Sorted and Rotated.
'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        # two possibilities:
        # 1. always non-decreasing
        # 2. one decreasing and nums[0] >= nums[-1]
        decreased = 0
        N = len(nums)
        for i in range(N - 1):
            if nums[i] > nums[i + 1]:
                decreased += 1
                if decreased > 1:
                    return False
        
        return True if 0 == decreased or (1 == decreased and nums[0] >= nums[-1]) else False



'''
approach: One Pass
Time: O(N)
Space: O(N)

Runtime: 28 ms, faster than 92.99% of Python3 online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 14.4 MB, less than 13.44% of Python3 online submissions for Check if Array Is Sorted and Rotated.

ref:
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/discuss/1053508/JavaC%2B%2BPython-Easy-and-Concise
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(a > b for a, b in zip(nums, nums[1: ] + nums[: 1])) <= 1


'''
approach: One Pass
Time: O(N)
Space: O(1)

Runtime: 24 ms, faster than 98.61% of Python3 online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 14 MB, less than 98.90% of Python3 online submissions for Check if Array Is Sorted and Rotated.
'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i - 1] for i in range(len(nums))) <= 1



'''
approach: One Pass + Sort
Time: O(N + NlogN) = O(NlogN)
Space: O(1)

Runtime: 28 ms, faster than 92.99% of Python3 online submissions for Check if Array Is Sorted and Rotated.
Memory Usage: 14.3 MB, less than 48.79% of Python3 online submissions for Check if Array Is Sorted and Rotated.
'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        for i in range(N):
            if nums[i] < nums[i - 1]:
                return nums[i: ] + nums[: i] == sorted(nums)
        return True