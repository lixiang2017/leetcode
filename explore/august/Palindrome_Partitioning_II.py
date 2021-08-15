'''
You are here!
Your runtime beats 30.39 % of python3 submissions.
You are here!
Your memory usage beats 98.49 % of python3 submissions.
'''
class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        cut = list(range(-1, N))
        
        for i in range(N):
            for j in range(i, N):
                if s[i: j] == s[j: i: -1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
                    
        return cut[-1]
