'''
执行用时：64 ms, 在所有 Python3 提交中击败了74.16% 的用户
内存消耗：24.3 MB, 在所有 Python3 提交中击败了40.73% 的用户
通过测试用例：77 / 77
'''
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        diff = abs(sum(nums) - goal)
        return (diff + limit - 1) // limit 
        