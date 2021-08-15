'''
Sort + Two Pointers,T:O(NlogN + N),S:O(1)

执行用时：164 ms, 在所有 Python3 提交中击败了92.60% 的用户
内存消耗：24.2 MB, 在所有 Python3 提交中击败了42.77% 的用户
'''
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] + nums[r] > target:
                r -= 1
            ans += r - l
            l += 1

        return ans % MOD