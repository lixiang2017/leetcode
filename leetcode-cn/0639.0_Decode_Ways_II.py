'''
DP
T: O(N)
S: O(N)

执行用时：1020 ms, 在所有 Python3 提交中击败了18.92% 的用户
内存消耗：23.8 MB, 在所有 Python3 提交中击败了5.40% 的用户
通过测试用例：217 / 217
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = [1, 1]
        dp2 = [0, 0]
        MOD = 10 ** 9 + 7

        for i, ch in enumerate(s):
            one = two = 0
            # one letter
            if ch == '0':
                one = 0
            elif '1' <= ch <= '9':
                one = dp1[-1] + dp2[-1]
            else: # *
                one = (dp1[-1] + dp2[-1]) * 9

            # two letters
            if i > 0:
                if s[i-1] in set(['0', '3', '4', '5', '6', '7', '8', '9']):
                    two = 0
                elif s[i-1: i+1] == '1*':
                    two = (dp1[-2] + dp2[-2]) * 9
                elif s[i-1: i+1] == '2*':
                    two = (dp1[-2] + dp2[-2]) * 6
                elif s[i-1] == '1':  # ch != '*'
                    two = dp1[-2] + dp2[-2]
                elif s[i-1: i+1] in set(['20', '21', '22', '23', '24', '25', '26']):
                    two = dp1[-2] + dp2[-2]
                elif s[i-1: i+1] in set(['27', '28', '29']):
                    two = 0
                elif s[i-1] == '*':
                    if ch == '*':
                        # 11 12 ... 19, 21 22 ...26, 9 + 6 = 15
                        two = (dp1[-2] + dp2[-2]) * 15
                    elif ch == '0':
                        # 10 20
                        two = (dp1[-2] + dp2[-2]) * 2
                    elif ch in set(['7', '8', '9']):
                        # 17 18 19
                        two = dp1[-2] + dp2[-2]
                    else:
                        # 1 ....6
                        two = (dp1[-2] + dp2[-2]) * 2

            dp1.append(one % MOD)
            dp2.append(two % MOD)

        return (dp1[-1] + dp2[-1]) % MOD
