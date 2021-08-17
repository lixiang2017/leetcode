'''
执行用时：24 ms, 在所有 Python3 提交中击败了99.09% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了70.99% 的用户
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        late = re.match('^[PAL]*LLL[PAL]*$', s)
        absent = re.match('^[^A]*A[^A]*A[PAL]*$', s)
        if not late and not absent:
            return True
        else:
            return False


'''
"PPALLP"
"PPALLL"
"LLLL"
"PLLPLLLLPP"
'''


'''
执行用时：28 ms, 在所有 Python3 提交中击败了94.53% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了22.08% 的用户
'''
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s
        