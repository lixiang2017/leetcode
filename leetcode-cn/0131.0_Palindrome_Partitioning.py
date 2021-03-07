'''
approach: Backtracking / DFS
Time: O(N * 2^N)
Space: O(N * 2^N)

执行用时：144 ms, 在所有 Python 提交中击败了80.47%的用户
内存消耗：48.2 MB, 在所有 Python 提交中击败了52.94%的用户
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        N = len(s)
        partitions = []
        part = []

        def isPalindrome(i, j):
            if i >= j:
                return True
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else False

        def dfs(i):
            if i == N:
                partitions.append(part[:])   # must have [:]
                return

            for j in range(i, N):
                if isPalindrome(i, j):
                    part.append(s[i : j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return partitions
