'''
T:O(2N),S:O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了71.29% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了84.94% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))


'''
T:O(logN),S:O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了45.18% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了65.86% 的用户
通过测试用例：34 / 34
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)
        while l <= r:
            mid = (l + r) // 2
            if mid > 0:
                if arr[mid] > arr[mid - 1]:
                    l = mid + 1
                elif arr[mid] < arr[mid - 1]:
                    r = mid - 1
            else:
                return 1
        return l - 1
