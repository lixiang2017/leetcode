'''
执行用时：152 ms, 在所有 Python3 提交中击败了50.94% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.66% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def dfs(x: int, y: int, cnt: int) -> None:
            nonlocal ans
            if cnt >= ans:
                return 
            if x >= n:
                ans = cnt 
                return 
            
            if y >= m:
                dfs(x + 1, 0, cnt)
                return 
            
            if rect[x][y]:
                dfs(x, y + 1, cnt)
                return 
            k = min(n - x, m - y)
            while k >= 1 and isAvailable(x, y, k):
                fillUp(x, y, k, True)
                dfs(x, y + k, cnt + 1)
                fillUp(x, y, k, False)
                k -= 1

        def isAvailable(x: int, y: int, k: int) -> bool:
            for i in range(k):
                for j in range(k):
                    if rect[x + i][y + j] == True:
                        return False
            return True 
        
        def fillUp(x: int, y: int, k: int, val: bool) -> None:
            for i in range(k):
                for j in range(k):
                    rect[x + i][y + j] = val 

        ans = max(n, m)
        rect = [[False] * m for _ in range(n)]
        dfs(0, 0, 0)
        return ans 
        