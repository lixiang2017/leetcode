'''
DFS

执行用时：48 ms, 在所有 Python3 提交中击败了13.90% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了18.99% 的用户
通过测试用例：277 / 277
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        OLD = image[sr][sc]
        COLOR = color 
        if OLD == color:
            return image 
            
        m, n = len(image), len(image[0])
        
        def fill(sr0, sc0):
            image[sr0][sc0] = COLOR 
            for nr, nc in [(sr0 - 1, sc0), (sr0 + 1, sc0), (sr0, sc0 - 1), (sr0, sc0 + 1)]:
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == OLD:
                    fill(nr, nc)

        fill(sr, sc)
        return image
