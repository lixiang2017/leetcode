'''
执行用时：32 ms, 在所有 Python3 提交中击败了69.79% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了41.70% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        for a, b, c in zip(text.split(), text.split()[1:], text.split()[2:]):
            if a == first and b == second:
                ans.append(c)
        return ans 
