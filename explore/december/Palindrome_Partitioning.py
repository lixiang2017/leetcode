'''
Approach: backtracking

You are here!
Your runtime beats 5.99 % of python submissions.

Time: O(N * 2 ^ N)
Space: O(N)
'''

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.dfs(s, [], result)
        return result
    
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)
    
    def isPal(self, s):
        return s == s[:: -1]
