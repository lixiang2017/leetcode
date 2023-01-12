'''
执行用时：124 ms, 在所有 Python3 提交中击败了95.76% 的用户
内存消耗：50.6 MB, 在所有 Python3 提交中击败了33.90% 的用户
通过测试用例：105 / 105
'''
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        stack = []
        know = {key: value for key, value in knowledge}
        for w in re.split('([()])', s):
            if w != ')':
                stack.append(w)
            else:
                w1 = stack.pop()
                left = stack.pop()
                stack.append(know.get(w1, '?'))

        return ''.join(stack)

   
        