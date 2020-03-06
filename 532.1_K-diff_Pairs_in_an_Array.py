'''
Success
Details 
Runtime: 128 ms, faster than 43.82% of Python online submissions for K-diff Pairs in an Array.
Memory Usage: 13.9 MB, less than 11.11% of Python online submissions for K-diff Pairs in an Array.
'''
from collections import Counter


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        c = Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1

        return res


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5]
    k = 2
    assert Solution().findPairs(nums, k) == 2

    nums = [1, 2, 3, 4, 5]
    k = 1
    assert Solution().findPairs(nums, k) == 4

    nums = [1, 3, 1, 5, 4]
    k = 0
    assert Solution().findPairs(nums, k) == 1

    nums = [5, 5, 5, 5, 5]
    k = 0
    assert Solution().findPairs(nums, k) == 1

    nums = [6, 6, 6, 7, 7]
    k = 0
    assert Solution().findPairs(nums, k) == 2
