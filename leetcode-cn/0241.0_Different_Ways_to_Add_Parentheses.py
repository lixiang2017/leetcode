'''
这样写， 会有重复结果。 之前分过组的， 可能会再次同样分组。

通过测试用例：15 / 25
输入：
"2*3-4*5"
输出：
[10,-14,-10,-10,-14,-34]
预期结果：
[-34,-10,-14,-10,10]

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

((2*3)-(4*5)) = -14 
这里，第一种是先 （2*3）-4*5， 后 （2*3）-（4*5）
第二种是先 2*3-（4*5）， 后 （2*3）-（4*5）
这两种其实同一种分组方法。
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        parts = []
        op2func = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }

        x = 0
        for ch in expression:
            if ch in '+-*':
                parts.append(x)
                parts.append(op2func[ch])
                x = 0
            else:
                x *= 10 
                x += ord(ch) - ord('0')
        parts.append(x)

        # "2*3-4*5" operator index only at 1, 3, 5, ...
        ans = []

        def backtrack(tokens):
            n = len(tokens)
            if 1 == n:
                ans.append(tokens[0])
                return 
            for i in range(1, n, 2):
                op_func = tokens[i]
                val = op_func(tokens[i - 1], tokens[i + 1])
                backtrack(tokens[: i - 1] + [val] + tokens[i + 2: ])

        backtrack(parts)
        return ans 



'''
左右分治处理，左右分别递归，就不会有重复了。

执行用时：40 ms, 在所有 Python3 提交中击败了66.86% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了54.18% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        parts = []
        op2func = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }

        x = 0
        for ch in expression:
            if ch in '+-*':
                parts.append(x)
                parts.append(op2func[ch])
                x = 0
            else:
                x *= 10 
                x += ord(ch) - ord('0')
        parts.append(x)

        # "2*3-4*5" operator index only at 1, 3, 5, ...

        @cache
        def dfs(l: int, r: int) -> List[int]:
            if l == r:
                return [parts[l]]

            possible = []
            # parts[i] is a operator
            for i in range(l + 1, r, 2):
                lefts = dfs(l, i - 1)
                rights = dfs(i + 1, r)
                op_func = parts[i]
                for left in lefts:
                    for right in rights:
                        possible.append(op_func(left, right))
            return possible

        return dfs(0, len(parts) - 1)


'''
recursion, just one function

执行用时：72 ms, 在所有 Python3 提交中击败了6.17% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了82.25% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i, ch in enumerate(expression):
            if ch.isdigit():
                continue
            lefts = self.diffWaysToCompute(expression[: i])
            rights = self.diffWaysToCompute(expression[i + 1: ])
            for l in lefts:
                for r in rights:
                    ans.append(eval(f'{l}{ch}{r}'))
        return ans 



'''
if ch not in '+-*'


执行用时：72 ms, 在所有 Python3 提交中击败了6.17% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了93.41% 的用户
通过测试用例：25 / 25
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        ans = []
        for i, ch in enumerate(expression):
            if ch not in '+-*':
                continue
            lefts = self.diffWaysToCompute(expression[: i])
            rights = self.diffWaysToCompute(expression[i + 1: ])
            for l in lefts:
                for r in rights:
                    ans.append(eval(f'{l}{ch}{r}'))
        return ans 



