'''
heap

59 / 59 个通过测试用例
状态：通过
执行用时: 692 ms
内存消耗: 25.5 MB
提交时间：6 小时前
'''
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = [-p for p in piles]
        heapq.heapify(h)
        while k:
            top = heappop(h)
            heappush(h, top + (-top // 2))
            k -= 1
        return -sum(h)
