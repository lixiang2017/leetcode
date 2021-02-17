'''
approach: Backtracking / DFS
Time: O(len(S))
Space: O(len(S)), ignore the return value

You are here!
Your runtime beats 81.16 % of python submissions.
You are here!
Your memory usage beats 26.03 % of python submissions.
'''


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        permuts = []
        S = S.lower()
        delta = ord('A') - ord('a')
        size = len(S)
        
        def backtracking(S, path, start, size):
            if len(path) == size:
                permuts.append(path)
                return
            
            backtracking(S, path + S[start], start + 1, size)
            if S[start].isalpha():
                backtracking(S, path + chr(ord(S[start]) + delta), start + 1, size)

        backtracking(S, '', 0, size)
        return permuts
        