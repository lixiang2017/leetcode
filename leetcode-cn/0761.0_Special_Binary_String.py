'''
recursion + stack

执行用时：40 ms, 在所有 Python3 提交中击败了66.67% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了80.30% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s 
        parts = []
        part = ''
        left = 0
        for ch in s:
            part += ch 
            if ch == '1':
                left += 1
            else:
                left -= 1
            if left == 0 and len(part) >= 2:
                parts.append('1' + self.makeLargestSpecial(part[1: -1]) + '0')
                part = ''

        return ''.join(sorted(parts, reverse=True))        
