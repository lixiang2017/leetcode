'''
TLE
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        isPalindrome = [[True] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                isPalindrome[i][j] = ((s[i] == s[j]) and isPalindrome[i + 1][j - 1])
        
        partitions = []
        part = []
        def backtracking(i):
            if i == N:
                partitions.append(part[:])
                return
            for j in range(i, N):
                if isPalindrome[i][j]:
                    part.append(s[i: j+1])
                    backtracking(j + 1)
                    part.pop()

        backtracking(0)
        return min([len(part) for part in partitions]) - 1


'''
"aab"
"cabababcbc"
'''

'''
24 / 29 个通过测试用例
状态：超出时间限制
提交时间：1 分钟内
最后执行的输入：
"ababababababababababababcbabababababababababababa"
'''




'''
approach: DP
Time: O(N^2)
Space: O(N^2)

执行用时：292 ms, 在所有 Python 提交中击败了84.93%的用户
内存消耗：29.1 MB, 在所有 Python 提交中击败了47.94%的用户
'''

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        isPalindrome = [[True] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                isPalindrome[i][j] = (s[i] == s[j]) and isPalindrome[i + 1][j - 1]
        
        cut = [float('inf')] * N
        for i in range(N):
            if isPalindrome[0][i]:
                cut[i] = 0
            else:
                for j in range(i):
                    if isPalindrome[j + 1][i]:
                        cut[i] = min(cut[i], cut[j] + 1)

        return cut[N - 1]
