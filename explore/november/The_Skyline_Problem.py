
'''
accepted. but i don't understand.
https://leetcode.com/problems/the-skyline-problem/discuss/954585/Python-O(n-log-n)-solution-using-heap-explained


You are here!
Your runtime beats 54.34 % of python submissions.
'''


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappop
        
        if not buildings:
            return []
        
        points = [(l, h, -1, i) for i, (l, r, h) in enumerate(buildings)]
        points += [(r, h, 1, i) for i, (l, r, h) in enumerate(buildings)]
        points.sort(key = lambda x: (x[0], x[1] * x[2]))
        heap, active, skyline = [(0, -1, -1)], set([-1]), []
        
        for x, h, lr, ind in points:
            if lr == -1: active.add(ind)
            else: active.remove(ind)
            
            if lr == -1:
                if h > -heap[0][0]:
                    skyline.append([x, h])
                heappush(heap, (-h, -x, ind)) 
            else:
                if h == -heap[0][0]:
                    while heap and heap[0][2] not in active: heappop(heap)
            if -heap[0][0] != skyline[-1][1]:
                skyline.append([x, -heap[0][0]])
        
        return skyline