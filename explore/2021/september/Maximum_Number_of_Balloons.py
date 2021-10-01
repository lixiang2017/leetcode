'''
You are here!
Your runtime beats 99.49 % of python3 submissions.
You are here!
Your memory usage beats 52.86 % of python3 submissions.
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])