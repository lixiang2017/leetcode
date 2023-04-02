'''
simulation

执行用时：48 ms, 在所有 Python3 提交中击败了7.79% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了84.42% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.split('@')
            return name[0].lower() + '*'*5 + name[-1].lower() + '@' + domain.lower()
        else:
            separation = {'+', '-', '(', ')', ' '}
            s = ''.join(ch for ch in s if ch not in separation)
            tail = s[-4:]
            if len(s) == 10:
                return '***-***-' + tail
            else:
                return '+' + '*' * (len(s) - 10)  + '-***-***-' + tail
