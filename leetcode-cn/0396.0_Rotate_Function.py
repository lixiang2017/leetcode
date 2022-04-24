'''
滚动更新/错位相减/滚动哈希(robin-karp算法)

执行用时：444 ms, 在所有 Python3 提交中击败了10.27% 的用户
内存消耗：21.7 MB, 在所有 Python3 提交中击败了85.93% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        ans = cur = total = 0
        for i, x in enumerate(nums):
            cur += i * x 
            total += x 

        ans = cur 
        for i in range(n - 1, -1 , -1):
            cur -= (n - 1) * nums[i]
            cur += total - nums[i]
            ans = max(ans, cur)
        return ans 
