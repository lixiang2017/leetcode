'''
hash table

执行用时：40 ms, 在所有 Python3 提交中击败了56.55%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了40.48%的用户
通过测试用例：42 / 42
'''
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)
        for i in range(n - 1):
            s = nums[i] + nums[i + 1]
            if s in seen:
                return True
            seen.add(s)
        return False
