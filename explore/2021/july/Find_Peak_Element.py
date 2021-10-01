'''
Time: O(N)
Space: O(1)

You are here!
Your memory usage beats 42.14 % of python3 submissions.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        elif len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i
        
        # still not found
        return 0 if nums[0] > nums[1] else len(nums) - 1
'''
Input: [1]
Output: None
Expected: 0


Input: [3,2,1]
Output: None
Expected: 0
'''

'''
approach 1: Linear Scan
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 78.08 % of python3 submissions.
You are here!
Your memory usage beats 70.76 % of python3 submissions.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1


'''
approach: Recursive Binary Search
Time: O(logN)
Space: O(logN)

You are here!
Your runtime beats 98.30 % of python3 submissions.
You are here!
Your memory usage beats 11.31 % of python3 submissions.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.search(nums, 0, len(nums) - 1)

    def search(self, nums, l, r):
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            return self.search(nums, l, mid)
            # return mid   # Wrong Answer 
        return self.search(nums, mid + 1, r)


'''
approach: Iterative Binary Search
Time: O(logN)
Space: O(1)

You are here!
Your runtime beats 78.08 % of python3 submissions.
You are here!
Your memory usage beats 70.76 % of python3 submissions.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l






