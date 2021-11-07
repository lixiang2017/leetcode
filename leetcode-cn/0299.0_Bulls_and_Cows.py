'''
hash table

执行用时：40 ms, 在所有 Python3 提交中击败了67.62% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了47.94% 的用户
通过测试用例：152 / 152
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # hash table for cows
        # s, g = defaultdict(int), defaultdict(int)
        s, g = [0] * 10, [0] * 10
        A = B = 0
        for ss, gg in zip(secret, guess):
            if ss == gg:
                A += 1
            else:
                s[ord(ss) - ord('0')] += 1
                g[ord(gg) - ord('0')] += 1
        B = sum([min(ss, gg) for ss, gg in zip(s, g)])
        return str(A) + 'A' + str(B) + "B"


'''
only one pass

执行用时：40 ms, 在所有 Python3 提交中击败了67.56% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了22.40% 的用户
通过测试用例：152 / 152
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        diff = [0] * 10
        A, B = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                if diff[ord(g) - ord('0')] > 0:
                    # have seen 's' before
                    B += 1
                if diff[ord(s) - ord('0')] < 0:
                    # have seen 'g' before
                    B += 1
                diff[ord(g) - ord('0')] -= 1
                diff[ord(s) - ord('0')] += 1

        return f'{A}A{B}B'
