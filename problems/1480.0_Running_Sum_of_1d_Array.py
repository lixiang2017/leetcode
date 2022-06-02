'''
T: O(N)
S: O(N)

Runtime: 62 ms, faster than 40.26% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.2 MB, less than 27.03% of Python3 online submissions for Running Sum of 1d Array.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))

'''
Runtime: 41 ms, faster than 86.96% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 13.9 MB, less than 94.41% of Python3 online submissions for Running Sum of 1d Array.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)


'''
T: O(N)
S: O(1)

Runtime: 82 ms, faster than 13.39% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.1 MB, less than 73.38% of Python3 online submissions for Running Sum of 1d Array.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

'''
T: O(N)
S: O(N)

Runtime: 43 ms, faster than 82.81% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.1 MB, less than 73.38% of Python3 online submissions for Running Sum of 1d Array.
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans, _sum = [], 0
        for x in nums:
            _sum += x 
            ans.append(_sum)
        return ans 
    
