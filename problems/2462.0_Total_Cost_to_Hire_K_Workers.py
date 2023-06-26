'''
heap + two pointers
T: O(N * log(candidates))
S: O(2 * candidates)

Runtime: 811 ms, faster than 70.20% of Python3 online submissions for Total Cost to Hire K Workers.
Memory Usage: 27.1 MB, less than 49.26% of Python3 online submissions for Total Cost to Hire K Workers.
'''
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total_cost = 0
        i, j = candidates - 1, max(candidates, n - candidates) 
        first = costs[: i + 1]
        last = costs[j: ]
        heapify(first)
        heapify(last)
        for _ in range(k):
            if first and last:
                if first[0] <= last[0]:
                    total_cost += heappop(first)
                else:
                    total_cost += heappop(last)
            elif first:
                total_cost += heappop(first)
            elif last:
                total_cost += heappop(last)
            
            if i + 1 <= j - 1:
                if len(first) < candidates:
                    heappush(first, costs[i + 1])
                    i += 1
                elif len(last) < candidates:
                    heappush(last, costs[j - 1])
                    j -= 1

        return total_cost


'''
Runtime: 864 ms, faster than 59.60% of Python3 online submissions for Total Cost to Hire K Workers.
Memory Usage: 27 MB, less than 81.88% of Python3 online submissions for Total Cost to Hire K Workers.
'''
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        ans = 0
        pre, post = [], []
        i, j = 0, n - 1
        for _ in range(k):
            while i <= j and len(pre) < candidates:
                heappush(pre, costs[i])
                i += 1
            while i <= j and len(post) < candidates:
                heappush(post, costs[j])
                j -= 1
            p0, p1 = pre[0] if pre else inf, post[0] if post else inf
            if p0 <= p1:
                ans += heappop(pre)
            else:
                ans += heappop(post)
                
        return ans 

