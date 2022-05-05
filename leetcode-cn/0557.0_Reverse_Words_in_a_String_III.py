'''
执行用时：24 ms, 在所有 Python3 提交中击败了98.80% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了98.57% 的用户
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda word: word[:: -1], s.split()))


'''
执行用时：40 ms, 在所有 Python3 提交中击败了67.86% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了68.96% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(''.join(list(reversed(w))) for w in s.split())

'''
执行用时：36 ms, 在所有 Python3 提交中击败了83.39% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了59.53% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(w[:: -1] for w in s.split())


'''
执行用时：108 ms, 在所有 Python3 提交中击败了5.67% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了78.20% 的用户
通过测试用例：29 / 29
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        i, n = 0, len(s)
        ans = ''
        while i < n:
            start = i 
            while i < n and s[i] != ' ':
                i += 1
            left, right = start, i - 1
            while right >= left:
                ans += s[right]
                right -= 1
            while i < n and s[i] == ' ':
                i += 1
                ans += ' '

        return ans 



        