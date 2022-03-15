'''
执行用时：40 ms, 在所有 Python3 提交中击败了26.87% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了87.11% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapify(h)
        while len(h) >= 2:
            # -8, -7    -10, -10
            x, y = heappop(h), heappop(h)
            if x != y:
                heappush(h, x - y)
                
        return -h[0] if h else 0
        