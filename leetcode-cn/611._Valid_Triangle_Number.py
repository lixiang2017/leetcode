'''
Sort + Two Pointers,T:O(N^2),S:O(1)
执行用时：1684 ms, 在所有 Python3 提交中击败了26.48% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了61.70% 的用户
'''
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        valid = 0
        nums.sort()
        N = len(nums)
        for i in range(N - 2):
            k = i + 2
            for j in range(i + 1, N - 1):
                if 0 == nums[i]:
                    continue
                while k < N and nums[i] + nums[j] > nums[k]:
                    k += 1
                valid += k - j - 1

        return valid
