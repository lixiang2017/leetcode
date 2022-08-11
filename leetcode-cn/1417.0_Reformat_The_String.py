'''
执行用时：44 ms, 在所有 Python3 提交中击败了80.63% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了21.17% 的用户
通过测试用例：302 / 302
'''
class Solution:
    def reformat(self, s: str) -> str:
        digit, letter = [], []
        for ch in s:
            if ch.isdigit():
                digit.append(ch)
            else:
                letter.append(ch)
        if abs(len(digit) - len(letter)) >= 2:
            return ''
        elif len(digit) == len(letter):
            return ''.join(a + b for a, b in zip(digit, letter))
        else:
            if len(digit) < len(letter):
                digit, letter = letter, digit
            return ''.join(a + b for a, b in zip_longest(digit, letter, fillvalue=''))
