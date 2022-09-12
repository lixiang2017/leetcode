'''
Greedy + Priority Queue + Sort
T: O(NlogN + NlogK)
S: O(N)

Runtime: 842 ms, faster than 18.57% of Python3 online submissions for Maximum Performance of a Team.
Memory Usage: 33.6 MB, less than 23.63% of Python3 online submissions for Maximum Performance of a Team.
'''
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        pairs = sorted(zip(speed, efficiency), key = lambda p: -p[1])
        ans, h, totals = 0, [], 0
        for s, e in pairs[: k - 1]:
            totals += s 
            heappush(h, s)
            ans = max(ans, totals * e)
        for s, e in pairs[k - 1: ]:
            totals += s 
            heappush(h, s)
            ans = max(ans, totals * e)
            totals -= heappop(h)
        return ans % MOD
