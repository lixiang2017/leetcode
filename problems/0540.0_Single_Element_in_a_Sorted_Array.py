'''
xor

Runtime: 64 ms, faster than 92.68% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.5 MB, less than 39.56% of Python3 online submissions for Single Element in a Sorted Array.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)


'''
xor

Runtime: 56 ms, faster than 99.48% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.4 MB, less than 39.56% of Python3 online submissions for Single Element in a Sorted Array.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans ^= x
        return ans


'''
Binary Search

Runtime: 122 ms, faster than 8.47% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.5 MB, less than 6.68% of Python3 online submissions for Single Element in a Sorted Array.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        N = len(nums)
        while l < r:
            mid = (l + r) // 2
            # exactly mid
            if (mid - 1 >= 0 and nums[mid] != nums[mid - 1]) and (mid + 1 < N and nums[mid] != nums[mid + 1]):
                return nums[mid]
            
            if (mid % 2 == 0 and mid + 1 < N and nums[mid] == nums[mid + 1]):
                l = mid + 2
            if (mid % 2 == 1 and mid - 1 >= 0 and nums[mid] == nums[mid - 1]):
                l = mid + 1
                
            if (mid % 2 == 1 and mid + 1 < N and nums[mid] == nums[mid + 1]):
                r = mid - 1
            if (mid % 2 == 0 and mid - 1 >= 0 and nums[mid] == nums[mid - 1]):
                r = mid - 2
            
        return nums[l]

'''
[1,1,2,3,3,4,4,8,8]
[3,3,7,7,10,11,11]
[1]
[1,1,2,3,3]
'''


'''
Binary Search

Runtime: 72 ms, faster than 56.14% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.5 MB, less than 39.56% of Python3 online submissions for Single Element in a Sorted Array.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                l = mid + 1
            else:
                r = mid
        
        return nums[l]


'''
Binary Search

Runtime: 79 ms, faster than 26.20% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 16.3 MB, less than 75.51% of Python3 online submissions for Single Element in a Sorted Array.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        
        return nums[l]


'''
binary search

Runtime: 182 ms, faster than 55.03% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 23.8 MB, less than 14.27% of Python3 online submissions for Single Element in a Sorted Array.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if mid & 1:
                mid -= 1
            if mid + 1 < n and nums[mid] == nums[mid + 1]:
                l = mid + 2
            elif mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                r = mid - 2
            else:
                return nums[mid]
        return nums[l]

'''
return nums[r]

Runtime: 179 ms, faster than 66.70% of Python3 online submissions for Single Element in a Sorted Array.
Memory Usage: 23.8 MB, less than 39.30% of Python3 online submissions for Single Element in a Sorted Array.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if mid & 1:
                mid -= 1
            if mid + 1 < n and nums[mid] == nums[mid + 1]:
                l = mid + 2
            elif mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                r = mid - 2
            else:
                return nums[mid]
        return nums[r]
