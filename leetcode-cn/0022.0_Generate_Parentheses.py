'''
Iteration

执行用时：44 ms, 在所有 Python3 提交中击败了56.75% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了13.70% 的用户
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set([''])
        for _ in range(n):
            next_ans = set()
            for one in ans:
                for j in range(len(one) + 1):
                    next_ans.add(one[:j] + '()' + one[j:])

            ans = next_ans
        return list(ans)
