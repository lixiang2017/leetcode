'''
max heap + simulation
T: O(N + NlogN)
S: O(N)

Runtime: 48 ms, faster than 42.93% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.8 MB, less than 68.03% of Python3 online submissions for Last Stone Weight.
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapify(h)
        while len(h) >= 2:
            s1 = -heappop(h)
            s2 = -heappop(h)
            heappush(h, s2 - s1)
        
        return -heappop(h)
        
'''
max heap + simulation
T: O(N + NlogN)
S: O(N)

Runtime: 49 ms, faster than 39.86% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.8 MB, less than 97.50% of Python3 online submissions for Last Stone Weight.
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapify(h)
        while len(h) >= 2:
            s1 = -heappop(h)
            s2 = -heappop(h)
            if s2 != s1:
                heappush(h, s2 - s1)
        
        return -heappop(h) if h else 0
        
'''
Runtime: 49 ms, faster than 39.86% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.8 MB, less than 68.03% of Python3 online submissions for Last Stone Weight.
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while len(stones) > 1:
            s = stones[-1] - stones[-2]
            del stones[-2: ]
            if s != 0:
                bisect.insort(stones, s)
        
        return next(iter(stones), 0)


'''
heap

Runtime: 40 ms, faster than 13.84% of Python3 online submissions for Last Stone Weight.
Memory Usage: 14 MB, less than 8.03% of Python3 online submissions for Last Stone Weight.1
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapify(h)
        while len(h) > 1:
            a, b = -heappop(h), -heappop(h)
            if a > b:
                heappush(h, b - a)
        return 0 if not h else -h[0]
        
