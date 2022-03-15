'''
hash set
T: O(N)
S: O(N)

执行用时：64 ms, 在所有 Python3 提交中击败了40.81% 的用户
内存消耗：25.6 MB, 在所有 Python3 提交中击败了24.13% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
