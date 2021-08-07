'''

执行用时：40 ms, 在所有 Python3 提交中击败了85.62% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了96.40% 的用户
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


'''
Math+String+Simulation

执行用时：104 ms, 在所有 Python3 提交中击败了55.87% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.13% 的用户
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        M, N = len(num1), len(num2)
        multi = [0] * (M + N)
        for i in range(M):
            for j in range(N):
                pos = M + N - (i + j) - 2
                multi[pos] += int(num1[i]) * int(num2[j])

        # carry
        for i in range(M + N -1):
            cur = multi[i]
            # left shift
            shift = 0
            while cur:
                cur, rem = divmod(cur, 10)
                if shift == 0:
                    multi[i] = rem
                else:
                    multi[i + shift] += rem
                shift += 1

        ans = ''.join(str(digit) for digit in multi).rstrip('0')[:: -1]
        if not ans:
            ans = '0'
        return ans

'''
输入：
"0"
"0"
输出：
""
预期结果：
"0"
'''
