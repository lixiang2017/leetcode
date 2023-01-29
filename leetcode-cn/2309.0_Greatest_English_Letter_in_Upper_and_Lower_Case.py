'''
bitwise

执行用时：56 ms, 在所有 Python3 提交中击败了24.89% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了9.50% 的用户
通过测试用例：113 / 113
'''
class Solution:
    def greatestLetter(self, s: str) -> str:
        occur = [0] * 26
        ans = ''
        for ch in s:
            idx = 0
            upper = ch 
            if 'a' <= ch <= 'z':
                idx = ord(ch) - ord('a')
                occur[idx] |= 1 
                upper = chr(ord(ch) - ord('a') + ord('A'))
            else:
                idx = ord(ch) - ord('A')
                occur[idx] |= 2
            if occur[idx] == 3 and (ans == '' or upper > ans):
                ans = upper  
        return ans 


'''
执行用时：36 ms, 在所有 Python3 提交中击败了90.05% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了30.77% 的用户
通过测试用例：113 / 113
'''
class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(s)
        ans = ''
        for l, u in zip(ascii_lowercase, ascii_uppercase):
            if l in seen and u in seen:
                ans = u 
        return ans 

