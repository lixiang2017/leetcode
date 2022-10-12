'''
sort + check
T: O(NlogN + N)
S: O(logN)

Runtime: 599 ms, faster than 5.00% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.5 MB, less than 45.85% of Python3 online submissions for Largest Perimeter Triangle.
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n - 2):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                ans = nums[i] + nums[i + 1] + nums[i + 2]
        return ans 

'''
sort + check
T: O(NlogN + N)
S: O(logN)

Runtime: 247 ms, faster than 80.28% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.5 MB, less than 45.85% of Python3 online submissions for Largest Perimeter Triangle.
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                ans = nums[i] + nums[i + 1] + nums[i + 2]
                break
        return ans 

'''
Runtime: 473 ms, faster than 21.21% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.3 MB, less than 91.63% of Python3 online submissions for Largest Perimeter Triangle.
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


'''
Runtime: 513 ms, faster than 11.46% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.4 MB, less than 45.85% of Python3 online submissions for Largest Perimeter Triangle.
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for (a, b), (_, c) in pairwise(zip(nums, nums[1: ])):
            if a < b + c:
                return a + b + c
        return 0


'''
Runtime: 199 ms, faster than 96.03% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.5 MB, less than 8.94% of Python3 online submissions for Largest Perimeter Triangle.
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for a, b, c in zip(nums, nums[1: ], nums[2: ]):
            if a < b + c:
                return a + b + c
        return 0
        
        