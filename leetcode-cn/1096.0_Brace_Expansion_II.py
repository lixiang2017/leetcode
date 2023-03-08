'''
执行用时：68 ms, 在所有 Python3 提交中击败了8.00% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了8.00% 的用户
通过测试用例：115 / 115
'''
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def dfs(exp):
            j = exp.find('}')
            if j == -1:
                s.add(exp)
                return
            i = exp.rfind('{', 0, j - 1)
            a, c = exp[: i], exp[j + 1: ]
            for b in exp[i + 1: j].split(','):
                dfs(a + b + c)

        s = set()      
        dfs(expression)
        return sorted(s)
        
        