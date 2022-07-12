'''
Runtime: 1330 ms, faster than 61.74% of Python3 online submissions for Matchsticks to Square.
Memory Usage: 186.4 MB, less than 5.04% of Python3 online submissions for Matchsticks to Square.
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ms = matchsticks
        ms.sort(reverse=True)
        n, s, edge = len(ms), sum(ms), sum(ms) // 4
        if s % 4 != 0 or ms[0] > edge:
            return False 
        
        @cache
        def dfs(idx, e1, e2, e3, e4):
            if idx == n:
                return e1 == e2 == e3 == e4 
            if max(e1, e2, e3, e4) > edge:
                return False 
            check = False
            check |= dfs(idx + 1, e1 + ms[idx], e2, e3, e4)
            check |= dfs(idx + 1, e1, e2 + ms[idx], e3, e4)
            check |= dfs(idx + 1, e1, e2, e3 + ms[idx], e4)
            check |= dfs(idx + 1, e1, e2, e3, e4 + ms[idx])
            return check
        
        return dfs(1, ms[0], 0, 0, 0)

'''
self.ans 

Details
Runtime: 1399 ms, faster than 61.39% of Python3 online submissions for Matchsticks to Square.
Memory Usage: 161.9 MB, less than 5.04% of Python3 online submissions for Matchsticks to Square.
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ms = matchsticks
        ms.sort(reverse=True)
        n, s, edge = len(ms), sum(ms), sum(ms) // 4
        if s % 4 != 0 or ms[0] > edge:
            return False
        
        self.ans = False
        
        @cache
        def dfs(idx, e1, e2, e3, e4):
            if self.ans:
                return True
            if idx == n:
                return e1 == e2 == e3 == e4 
            if max(e1, e2, e3, e4) > edge:
                return False 
            check = False
            check |= dfs(idx + 1, e1 + ms[idx], e2, e3, e4)
            check |= dfs(idx + 1, e1, e2 + ms[idx], e3, e4)
            check |= dfs(idx + 1, e1, e2, e3 + ms[idx], e4)
            check |= dfs(idx + 1, e1, e2, e3, e4 + ms[idx])
            if check:
                self.ans = True
            return check
        
        return dfs(1, ms[0], 0, 0, 0)


'''
not in 

Runtime: 216 ms, faster than 85.22% of Python3 online submissions for Matchsticks to Square.
Memory Usage: 33 MB, less than 10.78% of Python3 online submissions for Matchsticks to Square.
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ms = matchsticks
        ms.sort(reverse=True)
        n, s, edge = len(ms), sum(ms), sum(ms) // 4
        if s % 4 != 0 or ms[0] > edge:
            return False
        
        self.ans = False
        
        @cache
        def dfs(idx, e1, e2, e3, e4):
            if self.ans:
                return True
            if idx == n:
                return e1 == e2 == e3 == e4 
            if max(e1, e2, e3, e4) > edge:
                return False 
            check = False
            check |= dfs(idx + 1, e1 + ms[idx], e2, e3, e4)
            if e2 != e1:
                check |= dfs(idx + 1, e1, e2 + ms[idx], e3, e4)
            if e3 not in [e1, e2]:
                check |= dfs(idx + 1, e1, e2, e3 + ms[idx], e4)
            if e4 not in [e1, e2, e3]:
                check |= dfs(idx + 1, e1, e2, e3, e4 + ms[idx])
            if check:
                self.ans = True
            return check
        
        return dfs(1, ms[0], 0, 0, 0)


'''
Runtime: 152 ms, faster than 89.74% of Python3 online submissions for Matchsticks to Square.
Memory Usage: 14 MB, less than 56.70% of Python3 online submissions for Matchsticks to Square.
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        ms = matchsticks
        ms.sort(reverse=True)
        n, total = len(ms), sum(ms)
        edge = total // 4
        if n < 4 or ms[0] > edge or total % 4:
            return False
        self.ans = False

        def backtrack(s1, s2, s3, s4, i):
            if self.ans or (s1 == s2 == s3 == s4 and i == n):
                self.ans = True
                return  
            if s1 + ms[i] <= edge:
                backtrack(s1 + ms[i], s2, s3, s4, i + 1)
            if s2 + ms[i] <= edge and s2 != s1:
                backtrack(s1, s2 + ms[i], s3, s4, i + 1)
            if s3 + ms[i] <= edge and s3 not in (s1, s2):
                backtrack(s1, s2, s3 + ms[i], s4, i + 1)
            if s4 + ms[i] <= edge and s4 not in (s1, s2, s3):
                backtrack(s1, s2, s3, s4 + ms[i], i + 1)
        
        backtrack(ms[0], 0, 0, 0, 1)
        return self.ans



