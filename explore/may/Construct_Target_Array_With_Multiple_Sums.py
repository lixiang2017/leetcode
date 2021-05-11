'''
approach: Reversely(in a reversed way) + Heap
Time: O(???), sorry I don't know now.
Space: O(N)

You are here!
Your runtime beats 33.58 % of python3 submissions.
You are here!
Your memory usage beats 53.28 % of python3 submissions.
'''



import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        h = []
        total = sum(target)
        for num in target:
            heapq.heappush(h, -num)
        
        top = - h[0]
        while top > total - top:
            top = - heapq.heappop(h)
            left_total = total - top
            if 0 == left_total:
                heapq.heappush(h, -top)
                break
            top %= left_total
            if 0 == top:
                top = left_total
            total = left_total + top
            heapq.heappush(h, -top)
            top = -h[0]

        return h[0] == -1
    
'''
[1]
'''

