'''
执行用时：80 ms, 在所有 Python3 提交中击败了43.02% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了79.66% 的用户
通过测试用例：137 / 137
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        l, r = 0, n - 1
        i = n - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans[i] = nums[l] * nums[l]
                l += 1
            else:
                ans[i] = nums[r] * nums[r]
                r -= 1
            i -= 1

        return ans 
