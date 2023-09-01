'''
304 ms
15.9 MB
'''
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1 
        while total >= 0:
            c2 = total // cost2 
            ans += c2 + 1
            total -= cost1 
        return ans
        