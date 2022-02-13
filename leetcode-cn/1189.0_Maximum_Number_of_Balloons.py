'''
hash table

执行用时：36 ms, 在所有 Python3 提交中击败了62.72% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了58.58% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        return min(c['b'], c['a'], c['l']//2, c['o']//2, c['n'])
