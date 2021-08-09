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

'''
DP,k指针
T: O(2MN)
S: O(M+N)

执行用时：600 ms, 在所有 Python3 提交中击败了85.56% 的用户
内存消耗：18.4 MB, 在所有 Python3 提交中击败了86.11% 的用户
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * n
        dp[0] = 1
        pointers = [0] * len(primes)
        for i in range(1, n):
            ready = min([dp[pointers[idx]] * p for idx, p in enumerate(primes)]) 
            dp[i] = ready
            for idx, p in enumerate(primes):
                if dp[pointers[idx]] * p == ready:
                    pointers[idx] += 1
        return dp[-1]


'''
K路归并
heap

Runtime: 256 ms, faster than 92.04% of Python3 online submissions for Super Ugly Number.
Memory Usage: 17.9 MB, less than 84.92% of Python3 online submissions for Super Ugly Number.
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # (val, prime_idx, ugly_number_idx)
        # val = primes[prime_idx] * ans[ugly_number_idx]
        h = [(p, i, 0) for i, p in enumerate(primes)]
        heapq.heapify(h)
        ans = [0] * n
        ans[0] = 1
        
        # for j in range(1, n): # wrong
        j = 1
        while j < n:
            val, p_idx, i = heapq.heappop(h)
            if val != ans[j - 1]:
                ans[j] = val
                j += 1
            heappush(h, (ans[i + 1] * primes[p_idx], p_idx, i + 1))
        
        return ans[-1]


