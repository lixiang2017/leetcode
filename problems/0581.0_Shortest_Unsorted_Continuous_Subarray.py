'''
approach: Sort
Time: O(NlogN + N) = O(NlogN)
Space: O(N)

Runtime: 188 ms, faster than 49.18% of Python online submissions for Shortest Unsorted Continuous Subarray.
Memory Usage: 14.7 MB, less than 56.56% of Python online submissions for Shortest Unsorted Continuous Subarray.
'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from copy import copy
        snums = copy(nums)
        snums.sort()
        N = len(nums)
        minimum, maximum = N, 0
        for i in range(N):
            if snums[i] != nums[i]:
                minimum = min(minimum, i)
                maximum = max(maximum, i)
        
        diff = maximum - minimum + 1
        return diff if diff > 0 else 0


'''
approach: Two Monotone Stack/Queue (Increasing + Decreasing)
Time: O(N + N) = O(N)
Space: O(N)

Runtime: 240 ms, faster than 25.00% of Python online submissions for Shortest Unsorted Continuous Subarray.
Memory Usage: 14.5 MB, less than 96.31% of Python online submissions for Shortest Unsorted Continuous Subarray.
'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        N = len(nums)
        
        left, right = N, 0
        for i in range(N):
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)
        
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)
        
        diff = right - left + 1
        return diff if diff > 0 else 0

        # return right - left + 1 if right > left else 0    # also ok



'''
Brute Force
Time: O(N ^ 2)
Space:O(1)

209 / 307 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
[1,6922,4713,6615,750,3244,1685,2624,4439,5523,5803,8416,5460,336,1593,9714,42,1373,3353,3169,4253,5462,
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        left, right = N, 0
        for i in range(N - 1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    left = min(left, i)
                    right = max(right, j)
       
        return right - left + 1 if right > left else 0


'''
approach: Two Pointers
Time: O(N + N) = O(N)
Space: O(1)

Runtime: 184 ms, faster than 54.10% of Python online submissions for Shortest Unsorted Continuous Subarray.
Memory Usage: 14.4 MB, less than 96.31% of Python online submissions for Shortest Unsorted Continuous Subarray.
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        minimum, maximum = sys.maxint, -sys.maxint
        for i in range(N - 1):
            if nums[i] > nums[i + 1]:
                minimum = min(minimum, nums[i + 1])
                maximum = max(maximum, nums[i])
  
        left, right = 0, N - 1
        while left < N and nums[left] <= minimum:
            left += 1
        while right > left and nums[right] >= maximum:
            right -= 1
        
        return right - left + 1 if right > left else 0


'''
monotonic stack
T: O(2N)
S: O(2N)

Runtime: 417 ms, faster than 10.62% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
Memory Usage: 16.9 MB, less than 5.86% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left_mess = n
        # increasing stack, from left to right, (x, idx)
        stack = []
        for i, x in enumerate(nums):
            while stack and stack[-1][0] > x:
                left_mess = min(left_mess, stack.pop()[1])
            if not stack or stack[-1][0] <= x:
                stack.append((x, i))
        
        right_mess = -1
        # decreasing stak, from right to left, (x, idx)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while stack and stack[-1][0] < x:
                right_mess = max(right_mess, stack.pop()[1])
            if not stack or stack[-1][0] >= x:
                stack.append((x, i))
                
        return max(0, right_mess - left_mess + 1)
                

