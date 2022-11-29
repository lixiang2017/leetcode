'''
执行用时：48 ms, 在所有 Python3 提交中击败了87.50% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了60.63% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def minOperations(self, s: str) -> int:
        odd0 = odd1 = even0 = even1 = 0
        for i, ch in enumerate(s):
            if i & 1:
                if ch == '0':
                    odd0 += 1
                else:
                    odd1 += 1
            else:
                if ch == '0':
                    even0 += 1
                else:
                    even1 += 1
        # odd -> 0, even -> 1; even -> 0, odd -> 1
        return min(odd1 + even0, even1 + odd0)
        