'''
直接在开头判断三个位置 i mid j, 避免里面等于的讨论

binary search
T: O(logN)
S: O(1)

将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环. 

执行用时：44 ms, 在所有 Python3 提交中击败了14.77% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了84.58% 的用户
通过测试用例：195 / 195
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (j - i) // 2 + i 
            if nums[i] == target: return i 
            if nums[mid] == target: return mid 
            if nums[j] == target: return j 
            if nums[i] < nums[mid]:
                # 前半段更长，而且处于有序增长
                if nums[i] < target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                # 后半段更长，而且处于有序增长
                if nums[mid] < target < nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return -1


'''
T: O(N)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了68.70% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了61.73% 的用户
通过测试用例：195 / 195
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
