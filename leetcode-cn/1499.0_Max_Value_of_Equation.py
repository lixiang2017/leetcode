'''
执行用时：304 ms, 在所有 Python3 提交中击败了40.00% 的用户
内存消耗：53.2 MB, 在所有 Python3 提交中击败了51.43% 的用户
通过测试用例：66 / 66
'''
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -inf 
        q = deque()
        for x, y in points:
            while q and q[0][0] < x - k:
                q.popleft()
            if q:
                ans = max(ans, x + y + q[0][1])
            while q and q[-1][1] <= y - x:
                q.pop()
            q.append((x, y - x))
        return ans 
        