'''
执行用时：44 ms, 在所有 Python3 提交中击败了26.38% 的用户
内存消耗：21.1 MB, 在所有 Python3 提交中击败了81.21% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(operator.xor, nums)


'''
binary search

执行用时：44 ms, 在所有 Python3 提交中击败了26.38% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了69.27% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 0:
                if mid + 1 < n:
                    if nums[mid] == nums[mid + 1]:
                        l = mid + 2
                    else:
                        r = mid 
                elif mid - 1 >= 0:
                    if nums[mid - 1] == nums[mid]:
                        r = mid - 1
                    else:
                        l = mid
                else:
                    return nums[mid]
            else:
                if mid + 1 < n:
                    if nums[mid] == nums[mid + 1]:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif mid - 1 >= 0:
                    if nums[mid - 1] == nums[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    return nums[mid]

        return nums[l]


'''
binary search
仅考虑偶数下标

执行用时：36 ms, 在所有 Python3 提交中击败了68.59% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了69.57% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid 
        return nums[l]

'''
binary search
仅考虑偶数下标

执行用时：40 ms, 在所有 Python3 提交中击败了47.55% 的用户
内存消耗：21.1 MB, 在所有 Python3 提交中击败了83.53% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid 
        return nums[r]

'''
binary search
使用异或，可以避免多情况讨论

执行用时：44 ms, 在所有 Python3 提交中击败了26.50% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了73.50% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]



'''
执行用时：44 ms, 在所有 Python3 提交中击败了26.50% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了74.37% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid ^ 1]:
                l = mid + 1
            else:
                r = mid 
        return nums[r]

'''
执行用时：36 ms, 在所有 Python3 提交中击败了68.59% 的用户
内存消耗：21.1 MB, 在所有 Python3 提交中击败了84.62% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        idx = bisect_left(range(len(nums) - 1), True, key=lambda i: nums[i] != nums[i ^ 1])
        return nums[idx]


'''
执行用时：52 ms, 在所有 Python3 提交中击败了6.87% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了69.57% 的用户
通过测试用例：15 / 15
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n // 2):
            if nums[i * 2] != nums[i * 2 + 1]:
                return nums[i * 2]
        return nums[-1]

     
