'''
Iteration

You are here!
Your runtime beats 65.90 % of python3 submissions.
You are here!
Your memory usage beats 36.63 % of python3 submissions.
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = {''}
        for _ in range(n):
            next_ans = set()
            for one in ans:
                for j in range(len(one) + 1):
                    next_ans.add(one[:j] + '()' + one[j:])
            ans = next_ans
        return list(ans)
