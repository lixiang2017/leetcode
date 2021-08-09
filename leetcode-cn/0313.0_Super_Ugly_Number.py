'''
heap + set
T: O(MNlogMN)
S: O(2MN)

执行用时：604 ms, 在所有 Python3 提交中击败了85.19% 的用户
内存消耗：86.6 MB, 在所有 Python3 提交中击败了23.59% 的用户
'''

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = {1}
        h = [1]
        for _ in range(n):
            ugly = heapq.heappop(h)
            for prime in primes:
                nxt = ugly * prime
                if nxt not in seen:
                    seen.add(nxt)
                    heappush(h, nxt)

        return ugly

