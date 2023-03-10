'''
执行用时：116 ms, 在所有 Python3 提交中击败了83.95% 的用户
内存消耗：35.3 MB, 在所有 Python3 提交中击败了59.26% 的用户
通过测试用例：142 / 142

'''
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p
        if x == 0:
            return 0
        y = 0
        index = {0: -1}
        ans = len(nums)
        for i, v in enumerate(nums):
            y = (y + v) % p
            if (y - x) % p in index:
                ans = min(ans, i - index[(y - x) % p])
            index[y] = i 
        return ans if ans < len(nums) else -1
