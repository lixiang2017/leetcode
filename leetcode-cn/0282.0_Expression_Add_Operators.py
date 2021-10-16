'''
执行用时：9392 ms, 在所有 Python3 提交中击败了5.20% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了10.00% 的用户
通过测试用例：23 / 23
'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        ans = []
        for ops in product('+-* ', repeat = N - 1):
            expr = ''.join(i + j for i, j in zip(num, ops)).replace(' ', '') + num[-1]
            try:
                if '+00' not in expr and '-00' not in expr and '*00' not in expr and \
                        not expr.startswith('00') and eval(expr) == target:
                    ans.append(expr)
            except:
                pass
        return ans

'''
1+05
'''
