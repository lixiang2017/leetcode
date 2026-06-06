class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        ans = 0
        cost.sort(reverse=True)
        for i in range(0, n, 3):
            ans += cost[i]
            if i + 1 < n:
                ans += cost[i + 1]
        
        return ans

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost.sort(reverse=True)
        n = len(cost)
        for i in range(0, n, 3):
            ans += cost[i]
            if i + 1 < n:
                ans += cost[i + 1]
        return ans

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost.sort(reverse=True)
        n = len(cost)
        for i in range(n):
            if i % 3 != 2:
                ans += cost[i]
        return ans

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])     