'''
approach: Two Pointers
Time: O(N)
Space: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了82.61%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了96.27%的用户
'''


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        real = forward = 0
        while forward < N:
            if nums[forward] != val:
                nums[real] = nums[forward]
                real += 1
                forward += 1
            else:
                forward += 1
        return real
        