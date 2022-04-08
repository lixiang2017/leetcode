'''
执行用时：32 ms, 在所有 Python3 提交中击败了95.05% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了79.57% 的用户
通过测试用例：180 / 180
'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
        