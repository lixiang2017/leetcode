'''
T: O(2N)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了44.22% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了20.89% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))


'''
T: O(logN)
S: O(logN)

执行用时：28 ms, 在所有 Python3 提交中击败了89.55% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.21% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0

        def recursive(l, r):
            if l > r:
                return None
            if 0 == l and nums[0] > nums[1]:
                return 0
            if N - 1 == r and nums[r] > nums[r - 1]:
                return r

            m = (l + r) // 2
            if nums[m - 1] < nums[m] > nums[m + 1]:
                return m

            return recursive(l, m - 1) or recursive(m + 1, r)

        return recursive(0, len(nums) - 1)
