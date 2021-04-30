'''
approach: Hash Table
Time: O(N)
Space: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了68.60%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了24.33%的用户
'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        return [num for num, cnt in freq.items() if cnt == 1][0]
