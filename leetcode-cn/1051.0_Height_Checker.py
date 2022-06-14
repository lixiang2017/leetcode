'''
sort
T: O(NlogN + N)
S: O(logN)

执行用时：28 ms, 在所有 Python3 提交中击败了95.92% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了91.20% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for h, e in zip(heights, sorted(heights)) if h != e)

'''
执行用时：44 ms, 在所有 Python3 提交中击败了16.24% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了81.57% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum([h != e for h, e in zip(heights, expected)])
        