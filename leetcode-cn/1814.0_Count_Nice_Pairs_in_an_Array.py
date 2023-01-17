'''
hash table

执行用时：460 ms, 在所有 Python3 提交中击败了12.50% 的用户
内存消耗：23 MB, 在所有 Python3 提交中击败了73.86% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # 0 <= i < j < nums.length
        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        ## nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        MOD = 10 ** 9 + 7

        def rev(x):
            r = 0
            while x:
                x, d = divmod(x, 10)
                r = r * 10 + d 
            return r 
        
        ans = 0
        c = Counter()
        for x in nums:
            diff = x - rev(x)
            ans += c[diff]
            ans %= MOD 
            c[diff] += 1
        return ans 


