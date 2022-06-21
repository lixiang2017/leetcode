'''
执行用时：148 ms, 在所有 Python3 提交中击败了41.95% 的用户
内存消耗：25.6 MB, 在所有 Python3 提交中击败了37.36% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        remain, pq = 0, []
        n = len(heights)
        for i in range(n - 1):
            h0, h1 = heights[i], heights[i + 1]
            if h0 >= h1:
                continue 
            diff = h1 - h0 
            heappush(pq, diff)
            if len(pq) > ladders:
                remain += heappop(pq)
                if remain > bricks:
                    return i 
        return n - 1
        