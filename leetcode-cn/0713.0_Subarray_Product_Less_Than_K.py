'''
只需要计算包含最右边的数字的子串数量，就不会重复了

执行用时：164 ms, 在所有 Python3 提交中击败了45.70% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了40.32% 的用户
通过测试用例：97 / 97
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < min(nums):
            return 0
        # product
        prod = 1
        n = len(nums)
        l = r = 0
        ans = 0
        while r < n:
            prod *= nums[r]
            while l <= r and l < n and prod >= k:
                prod //= nums[l]
                l += 1
            # [l, r]
            ans += (r - l + 1)
            # move
            r += 1

        return ans 
