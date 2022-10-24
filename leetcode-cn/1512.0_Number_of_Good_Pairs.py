'''
执行用时：36 ms, 在所有 Python3 提交中击败了74.73% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了24.62% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        ans = 0
        for _, cnt in c.items():
            ans += cnt * (cnt - 1) // 2
        return ans 
        