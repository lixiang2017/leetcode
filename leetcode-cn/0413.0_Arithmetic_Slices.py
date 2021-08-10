'''
Two Pointers,T:O(N),S:O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了79.52% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了73.57% 的用户
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        N = len(nums)
        i = j = 0
        while i < N - 2:
            j = i + 1
            diff = nums[j] - nums[i]
            cnt = 1
            while j < N - 1 and nums[j + 1] - nums[j] == diff:
                cnt += 1
                j += 1
            if cnt > 1:
                total += cnt * (cnt - 1) // 2

            i = j

        return total

'''
DP,T:O(N),S:O(1)
执行用时：28 ms, 在所有 Python3 提交中击败了93.12% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了37.75% 的用户
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        total = i = j = 0
        while i < N - 2:
            j = i
            diff = nums[j + 1] - nums[j]
            cnt = 0
            while j < N - 1 and nums[j + 1] - nums[j] == diff:
                total += cnt
                cnt += 1
                j += 1
            i = j
        return total
