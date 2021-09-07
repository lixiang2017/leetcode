'''
Greedy + Heap


执行用时：276 ms, 在所有 Python3 提交中击败了73.29% 的用户
内存消耗：34.9 MB, 在所有 Python3 提交中击败了65.75% 的用户
通过测试用例：35 / 35
'''
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        N = len(profits)
        cp = [(c, p) for c, p in zip(capital, profits)]
        cp.sort()

        # init heap
        h = []
        i = 0
        while i < N and cp[i][0] <= w:
            heappush(h, -cp[i][1])
            i += 1
        
        while k > 0 and len(h) > 0:
            w += -heappop(h)
            while i < N and cp[i][0] <= w:
                heappush(h, -cp[i][1])
                i += 1
            k -= 1

        return w
