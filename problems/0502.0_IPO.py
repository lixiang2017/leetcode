'''
heap

Runtime: 1107 ms, faster than 47.38% of Python3 online submissions for IPO.
Memory Usage: 38.9 MB, less than 42.66% of Python3 online submissions for IPO.
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 以 capital 为中心，在 capital 允许的情况下，考虑最大 profit
        i, n = 0, len(profits)
        cp = [(c, p) for c, p in zip(capital, profits)]
        cp.sort()
        # profit 放入 heap 中，而且只是放入当前w 可以拿到的 profit
        # 同时根据当前 w，动态得向 heap 中添加可以拿到的profit
        ## init heap
        h = []
        while i < n and cp[i][0] <= w:
            heappush(h, -cp[i][1])
            i += 1
        
        ## pick k projects
        while k and h:
            w -= heappop(h)
            while i < n and cp[i][0] <= w:
                heappush(h, -cp[i][1])
                i += 1
            k -= 1
        
        return w
        

'''
Runtime: 1111 ms, faster than 46.50% of Python3 online submissions for IPO.
Memory Usage: 38.8 MB, less than 42.66% of Python3 online submissions for IPO.
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ptr, n = 0, len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        q = []
        for _ in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break
            w -= heappop(q)
        return w
        


        