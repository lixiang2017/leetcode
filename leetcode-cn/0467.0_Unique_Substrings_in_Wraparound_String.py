'''
记录以每种字符结尾最长子串的长度
以每种字符结尾最长子串数目 之和 -> ans 

DP
T: O(26N)
S: O(26)

执行用时：96 ms, 在所有 Python3 提交中击败了42.11% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了16.14% 的用户
通过测试用例：81 / 81
'''

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p += p[-1]
        # max length for each letter, substring endswith this letter
        max_len = [0] * 26
        n = len(p)
        cur_len = 1
        idx = {ch: ord(ch) - ord('a') for ch in string.ascii_lowercase}

        for i in range(1, n):
            if (idx[p[i - 1]] + 1) % 26 == idx[p[i]]:
                cur_len += 1
            else:
                # ...cur_len...(i-1)
                step = 1
                while step <= 26 and cur_len >= 1:
                    ch = p[i - step]
                    max_len[idx[ch]] = max(max_len[idx[ch]], cur_len)
                    cur_len -= 1
                    step += 1
                cur_len = 1

        return sum(max_len)


'''
记录以每种字符结尾最长子串的长度
以每种字符结尾最长子串数目 之和 -> ans 

DP
T: O(N)
S: O(26)

执行用时：92 ms, 在所有 Python3 提交中击败了51.23% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了77.19% 的用户
通过测试用例：81 / 81
'''

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p += p[-1]
        # max length for each letter, substring endswith this letter
        max_len = [0] * 26
        n = len(p)
        cur_len = 1
        idx = {ch: ord(ch) - ord('a') for ch in string.ascii_lowercase}
        max_len[idx[p[0]]] = 1

        for i in range(1, n):
            if (idx[p[i - 1]] + 1) % 26 == idx[p[i]]:
                cur_len += 1
            else:
                cur_len = 1
            ch = p[i]
            max_len[idx[ch]] = max(max_len[idx[ch]], cur_len)

        return sum(max_len)
            

'''
记录以每种字符结尾最长子串的长度
以每种字符结尾最长子串数目 之和 -> ans 

no need to use p += p[-1]
执行用时：84 ms, 在所有 Python3 提交中击败了75.09% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了75.44% 的用户
通过测试用例：81 / 81
'''

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # max length for each letter, substring endswith this letter
        max_len = [0] * 26
        n = len(p)
        cur_len = 1
        idx = {ch: ord(ch) - ord('a') for ch in string.ascii_lowercase}
        max_len[idx[p[0]]] = 1

        for i in range(1, n):
            if (idx[p[i - 1]] + 1) % 26 == idx[p[i]]:
                cur_len += 1
            else:
                cur_len = 1
            ch = p[i]
            max_len[idx[ch]] = max(max_len[idx[ch]], cur_len)

        return sum(max_len)
            
'''
执行用时：108 ms, 在所有 Python3 提交中击败了23.86% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了68.42% 的用户
通过测试用例：81 / 81
'''
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[ch] = max(dp[ch], k)
        return sum(dp.values())
        