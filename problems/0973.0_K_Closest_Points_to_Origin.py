'''
heap

Runtime: 685 ms, faster than 56.71% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 19.9 MB, less than 63.87% of Python3 online submissions for K Closest Points to Origin.
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i, p in enumerate(points):
            d = p[0] * p[0] + p[1] * p[1]
            if i < k:
                heappush(h, (-d, p))
            else:
                heappush(h, (-d, p))
                heappop(h)
        return [p for _d, p in h]

'''
Runtime: 648 ms, faster than 83.09% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 20.3 MB, less than 31.45% of Python3 online submissions for K Closest Points to Origin.
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])
        