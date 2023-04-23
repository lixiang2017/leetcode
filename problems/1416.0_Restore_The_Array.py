'''
DP

Runtime: 1586 ms, faster than 61.64% of Python3 online submissions for Restore The Array.
Memory Usage: 18.1 MB, less than 86.30% of Python3 online submissions for Restore The Array.
'''
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        MOD = 10 ** 9 + 7
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n):
            x = 0
            for j in range(i, i + 10):
                if j >= n:
                    break
                x *= 10
                x += ord(s[j]) - ord('0')
                if x > k or (x == 0 and i == j):
                    break
                if x <= 0:
                    continue
                f[j + 1] += f[i]
                f[j + 1] %= MOD
        return f[n]


'''
            # starts with s[i]
            if s[i] == '0':
                continue

Runtime: 1432 ms, faster than 78.08% of Python3 online submissions for Restore The Array.
Memory Usage: 18.3 MB, less than 71.23% of Python3 online submissions for Restore The Array.
'''
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        MOD = 10 ** 9 + 7
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n):
            # starts with s[i]
            if s[i] == '0':
                continue
            x = 0
            for j in range(i, i + 10):
                if j >= n:
                    break
                x *= 10
                x += ord(s[j]) - ord('0')
                if x > k:
                    break
                f[j + 1] += f[i]
                f[j + 1] %= MOD
        return f[n]

'''
                if x <= 0 or x > k:
                    break

Runtime: 1553 ms, faster than 67.12% of Python3 online submissions for Restore The Array.
Memory Usage: 18.2 MB, less than 82.19% of Python3 online submissions for Restore The Array.
'''
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        MOD = 10 ** 9 + 7
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n):
            # starts with s[i]
            x = 0
            for j in range(i, i + 10):
                if j >= n:
                    break
                x *= 10
                x += ord(s[j]) - ord('0')
                if x <= 0 or x > k:
                    break
                f[j + 1] += f[i]
                f[j + 1] %= MOD
        return f[n]

'''
for j in range(i, min(n, i + 10))

Runtime: 1518 ms, faster than 69.86% of Python3 online submissions for Restore The Array.
Memory Usage: 18.2 MB, less than 82.19% of Python3 online submissions for Restore The Array.
'''
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        MOD = 10 ** 9 + 7
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(n):
            # starts with s[i]
            x = 0
            for j in range(i, min(n, i + 10)):
                x *= 10
                x += ord(s[j]) - ord('0')
                if x == 0 or x > k:
                    break
                f[j + 1] += f[i]
                f[j + 1] %= MOD
        return f[n]
