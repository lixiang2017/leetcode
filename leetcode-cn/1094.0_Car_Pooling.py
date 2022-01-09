'''
Prefix Sum
T: O(N + 1000)
S: O(1000)

执行用时：32 ms, 在所有 Python3 提交中击败了92.94% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了15.47% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for numi, fromi, toi in trips:
            diff[fromi] += numi 
            diff[toi] -= numi 
        presum = 0
        for i in range(1001):
            presum += diff[i]
            if presum > capacity:
                return False
        return True 

'''
heapq + Prefix Sum

执行用时：44 ms, 在所有 Python3 提交中击败了33.86% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.48% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h1 = [(fromi, numi) for numi, fromi, toi in trips]
        h2 = [(toi, -numi) for numi, fromi, toi in trips]
        h = h1 + h2 
        heapify(h)
        presum = 0
        while h:
            location, x = heappop(h)
            presum += x 
            if presum > capacity:
                return False
        return True 

'''
sort

执行用时：48 ms, 在所有 Python3 提交中击败了24.00% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了5.48% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h1 = [(fromi, numi) for numi, fromi, toi in trips]
        h2 = [(toi, -numi) for numi, fromi, toi in trips]
        h = h1 + h2 
        h.sort()
        presum = 0
        for loc, x in h:
            presum += x
            if presum > capacity:
                return False
        return True             





'''
sort + heapq
执行用时：40 ms, 在所有 Python3 提交中击败了56.03% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了61.51% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t: t[1])
        h = []
        passengers = 0
        for numi, fromi, toi in trips:
            while h and h[0][0] <= fromi:
                tox, numx = heappop(h)
                passengers -= numx 
            passengers += numi 
            if passengers > capacity:
                return False 
            heappush(h, (toi, numi))

        return True 

