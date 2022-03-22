'''
执行用时：40 ms, 在所有 Python3 提交中击败了36.59% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了96.38% 的用户
通过测试用例：27 / 27
'''
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total, last = 1, 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if last + w > 100:
                total += 1
                last = w
            else:
                last += w

        return [total, last]
        