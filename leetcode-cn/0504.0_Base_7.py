'''
执行用时：36 ms, 在所有 Python3 提交中击败了53.77% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了15.85% 的用户
通过测试用例：241 / 241
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
            
        negative = False
        if num < 0:
            negative = True
            num = -num

        q = deque()
        while num:
            num, rem = divmod(num, 7)
            q.appendleft(str(rem))

        return ('-' if negative else '') + ''.join(q)
        

