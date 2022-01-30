'''
执行用时：60 ms, 在所有 Python3 提交中击败了12.24% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了22.63% 的用户
通过测试用例：244 / 244
'''
class Solution:
    def countValidWords(self, sentence: str) -> int:
        ans = 0
        for w in sentence.split():
            if re.match('^[a-z]*[!.,]?$|^[a-z]+-[a-z]+[!.,]?$', w):
                ans += 1
        return ans
        