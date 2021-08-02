'''
sort,T:O(NlogN),S:O(N)
执行用时：52 ms, 在所有 Python3 提交中击败了88.82% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了58.77% 的用户
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n2 = sorted(nums)
        l, r = 0, len(n2) - 1
        while l <= r and nums[l] == n2[l]:
            l += 1
        while l <= r and nums[r] == n2[r]:
            r -= 1
        return r - l + 1
        