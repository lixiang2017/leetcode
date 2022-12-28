'''
heap

Runtime: 1720 ms, faster than 97.60% of Python3 online submissions for Remove Stones to Minimize the Total.
Memory Usage: 28.6 MB, less than 67.75% of Python3 online submissions for Remove Stones to Minimize the Total.
'''
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-p for p in piles]
        heapify(h)
        while k:
            x = h[0] + (-h[0]) // 2
            heapreplace(h, x)
            k -= 1
        return -sum(h)
