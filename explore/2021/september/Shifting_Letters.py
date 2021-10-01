'''
Time: O(6N)

You are here!
Your runtime beats 19.48 % of python3 submissions.
You are here!
Your memory usage beats 39.08 % of python3 submissions.
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        postsum = reversed(list(accumulate(reversed(shifts))))
        MOD = 26
        ans = []
        for ch, shift in zip(s, postsum):
            delta = (ord(ch) - ord('a') + shift) % MOD
            newchr = chr(delta + ord('a'))
            ans.append(newchr)
        return ''.join(ans)


'''
Time: O(2N)

You are here!
Your runtime beats 18.73 % of python3 submissions.
You are here!
Your memory usage beats 19.98 % of python3 submissions.
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        MOD = 26
        ans = ''
        post = 0
        for i in range(len(shifts) - 1, -1, -1):
            post = (post + shifts[i]) % MOD
            ans += chr( (post + ord(s[i]) - ord('a')) % MOD + ord('a') )
        return ans[:: -1]
