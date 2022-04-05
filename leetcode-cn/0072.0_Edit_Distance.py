'''
dp, T: O(MN), S: O(MN)

执行用时：148 ms, 在所有 Python3 提交中击败了71.70% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了22.89% 的用户
通过测试用例：1146 / 1146
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # the first row
        for j in range(1, n2 + 1):
            dp[0][j] = j
        # the first column
        for i in range(1, n1 + 1):
            dp[i][0] = i 
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]


'''
DFS with memorization
字符串切片会有 O(N)

执行用时：116 ms, 在所有 Python3 提交中击败了94.24% 的用户
内存消耗：30 MB, 在所有 Python3 提交中击败了5.01% 的用户
通过测试用例：1146 / 1146
'''
class Solution:
    @lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) + len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1: ], word2[1: ])
        else:
            insert = self.minDistance(word1, word2[1: ])
            delete = self.minDistance(word1[1: ], word2)
            replace = self.minDistance(word1[1: ], word2[1: ])
            return 1 + min(insert, delete, replace)


'''
执行用时：88 ms, 在所有 Python3 提交中击败了97.69% 的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了92.06% 的用户
通过测试用例：1146 / 1146
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        @lru_cache(None)
        def helper(i, j):
            if i == n1 or j == n2:
                return (n1 - i) + (n2 - j)
            if word1[i] == word2[j]:
                return helper(i + 1, j + 1)
            else:
                insert = helper(i, j + 1)
                delete = helper(i + 1, j)
                replace = helper(i + 1, j + 1)
                return 1 + min(insert, delete, replace)
        
        return helper(0, 0)

'''
DFS, from n1 n2 to 0 0

执行用时：76 ms, 在所有 Python3 提交中击败了99.37% 的用户
内存消耗：17.8 MB, 在所有 Python3 提交中击败了91.52% 的用户
通过测试用例：1146 / 1146
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        @lru_cache(None)
        def helper(i, j):
            if 0 == i or 0 == j:
                return i + j
            if word1[i - 1] == word2[j - 1]:
                return helper(i - 1, j - 1)
            else:
                insert = helper(i, j - 1)
                delete = helper(i - 1, j)
                replace = helper(i - 1, j - 1)
                return 1 + min(insert, delete, replace)
        
        return helper(n1, n2)


'''
DFS, from n1-1 n2-1 to -1 -1

执行用时：80 ms, 在所有 Python3 提交中击败了98.99% 的用户
内存消耗：17.9 MB, 在所有 Python3 提交中击败了91.04% 的用户
通过测试用例：1146 / 1146
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        @lru_cache(None)
        def helper(i, j):
            if -1 == i or -1 == j:
                return i + j + 2
            if word1[i] == word2[j]:
                return helper(i - 1, j - 1)
            else:
                insert = helper(i, j - 1)
                delete = helper(i - 1, j)
                replace = helper(i - 1, j - 1)
                return 1 + min(insert, delete, replace)
        
        return helper(n1 - 1, n2 - 1)

