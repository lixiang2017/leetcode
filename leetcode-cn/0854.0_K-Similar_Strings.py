'''
backtrack + prune
碰巧压线可以通过

执行用时：6800 ms, 在所有 Python3 提交中击败了5.66% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了94.34% 的用户
通过测试用例：62 / 62
'''
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        ss1, ss2 = list(s1), list(s2)
        n = len(ss1)
        ans = float('inf')

        def backtrack(i, ss1, ss2, swap):
            nonlocal ans 
            if swap >= ans: # prune
                return 
            while i < n and ss1[i] == ss2[i]:
                i += 1
            if i == n:
                ans = min(ans, swap)   
                return 
            # ss1[i] != ss2[i], to swap
            for j in range(i + 1, n):
                if ss2[j] == ss1[i]:
                    ss2[i], ss2[j] = ss2[j], ss2[i]
                    backtrack(i + 1, ss1, ss2, swap + 1)
                    ss2[i], ss2[j] = ss2[j], ss2[i]

        backtrack(0, ss1, ss2, 0)
        return ans 

