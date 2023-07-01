'''
backtrack

Runtime: 2196 ms, faster than 28.73% of Python3 online submissions for Fair Distribution of Cookies.
Memory Usage: 16.3 MB, less than 51.49% of Python3 online submissions for Fair Distribution of Cookies.
'''
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        n = len(cookies)
        ans = sum(cookies)
        
        def backtrack(i, distribution):
            if i == n:
                nonlocal ans
                ans = min(max(distribution), ans)
                return 
            for j in range(k):
                if distribution[j] + cookies[i] >= ans:
                    continue
                distribution[j] += cookies[i]
                backtrack(i + 1, distribution)
                distribution[j] -= cookies[i]

        backtrack(0, distribution)
        return ans 

'''
backtrack

Runtime: 2122 ms, faster than 28.73% of Python3 online submissions for Fair Distribution of Cookies.
Memory Usage: 16.4 MB, less than 51.49% of Python3 online submissions for Fair Distribution of Cookies.
'''
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribution = [0] * k
        n = len(cookies)
        ans = sum(cookies)
        
        def backtrack(i):
            if i == n:
                nonlocal ans
                ans = min(max(distribution), ans)
                return 
            for j in range(k):
                if distribution[j] + cookies[i] >= ans:
                    continue
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]

        backtrack(0)
        return ans 

'''
Runtime: 1131 ms, faster than 52.24% of Python3 online submissions for Fair Distribution of Cookies.
Memory Usage: 16.4 MB, less than 21.27% of Python3 online submissions for Fair Distribution of Cookies.
'''
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        if k >= n:
            return max(cookies)
        
        distribution = [0] * k
        ans = sum(cookies)
        
        def backtrack(i):
            if i == n:
                nonlocal ans
                ans = min(max(distribution), ans)
                return 
            for j in range(k):
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]

        backtrack(0)
        return ans 

'''
Runtime: 52 ms, faster than 93.28% of Python3 online submissions for Fair Distribution of Cookies.
Memory Usage: 16.4 MB, less than 51.49% of Python3 online submissions for Fair Distribution of Cookies.
'''
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        if k >= n:
            return max(cookies)
        
        distribution = [0] * k
        ans = sum(cookies)
        
        def backtrack(i):
            if i == n:
                nonlocal ans
                ans = min(max(distribution), ans)
                return 
            for j in range(k):
                if distribution[j] + cookies[i] >= ans:
                    continue
                distribution[j] += cookies[i]
                backtrack(i + 1)
                distribution[j] -= cookies[i]

        backtrack(0)
        return ans 
