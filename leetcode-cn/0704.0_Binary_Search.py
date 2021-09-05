'''
BS

执行用时：40 ms, 在所有 Python3 提交中击败了64.67% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了84.07% 的用户
通过测试用例：46 / 46
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


'''
index

执行用时：44 ms, 在所有 Python3 提交中击败了41.31% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了73.92% 的用户
通过测试用例：46 / 46
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1

'''
bisect_left

执行用时：32 ms, 在所有 Python3 提交中击败了94.66% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了88.11% 的用户
通过测试用例：46 / 46
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = bisect_left(nums, target)
        return x if x != len(nums) and target == nums[x] else -1


'''
bisect_right

执行用时：40 ms, 在所有 Python3 提交中击败了64.67% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了72.54% 的用户
通过测试用例：46 / 46
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = bisect_right(nums, target)
        return x - 1 if target == nums[x-1] else -1
