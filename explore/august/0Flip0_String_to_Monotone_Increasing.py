'''
two pass
T: O(2N)
S: O(2N)

You are here!
Your memory usage beats 7.58 % of python3 submissions.
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        ans = N
        zero, one = [0] * N, [0] * N
        # prefix sum 0s, from right to left
        for i in range(N - 1, -1 , -1):
            if i == N - 1:
                if s[i] == '0':
                    zero[i] = 1
            else:
                if s[i] == '0':
                    zero[i] = zero[i + 1] + 1
                else:
                    zero[i] = zero[i + 1] 
        # prefix sum 1s, from left to right
        for i in range(N):
            if i == 0:
                if s[i] == '1':
                    one[i] = 1
            else:
                if s[i] == '1':
                    one[i] = one[i - 1] + 1
                else:
                    one[i] = one[i - 1]
        # update
        for i in range(N):
            ans = min(ans, (zero[i] + one[i]) - 1)
        return ans
