'''
brute force

执行用时：3576 ms, 在所有 Python3 提交中击败了5.19% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了83.12% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        m, n = len(s), len(t)

        def diff(i, j, l):
            return sum(s[i + k] != t[j + k] for k in range(l))

        for l in range(1, min(m, n) + 1):
            for i in range(m - l + 1):
                for j in range(n - l + 1):
                    if diff(i, j, l) == 1:
                        ans += 1
        return ans 

'''
for-for-while

执行用时：80 ms, 在所有 Python3 提交中击败了37.66% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.40% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        m, n = len(s), len(t)

        for i in range(m):
            for j in range(n):
                k = diff = 0
                while i + k < m and j + k < n and diff < 2:
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        ans += 1
                    k += 1
        return ans 


'''
hash table

执行用时：8604 ms, 在所有 Python3 提交中击败了5.19% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了28.57% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ans = 0
        m, n = len(s), len(t)
        c = Counter()
        for i in range(n):
            for l in range(1, n - i + 1):
                c[t[i: i + l]] += 1

        for i in range(m):
            for l in range(1, m - i + 1):
                for k in range(l):
                    for ch in string.ascii_lowercase:
                        if ch == s[i + k]:
                            continue
                        substr = s[i: i + k] + ch + s[i + k + 1: i + l]
                        ans += c[substr]
 
        return ans 


