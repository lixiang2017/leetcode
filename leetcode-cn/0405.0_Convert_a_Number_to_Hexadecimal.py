'''
执行用时：24 ms, 在所有 Python3 提交中击败了96.67% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.36% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def toHex(self, num: int) -> str:
        b = ''
        for i in range(31, -1, -1):
            b += str(1 if num & (1 << i) else 0)
        m = '0123456789abcdef'
        ans = ''
        for i in range(0, 32, 4):
            ans += m[int(b[i: i+4], 2)]
        while ans[0] == '0' and len(ans) > 1:
            ans = ans[1:]
        return ans

'''
26
-1
-2
-3
b:
00000000000000000000000000011010
11111111111111111111111111111111
11111111111111111111111111111110
11111111111111111111111111111101
'''
