'''
simulation
T: O(MN)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了96.94% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了57.14% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        # ball
        for b in range(n):
            for r in range(m):
                if grid[r][b] == 1:
                    if b + 1 < n and grid[r][b + 1] == 1:
                        b += 1
                    else:
                        b = -1
                        break 
                else:
                    if b - 1 >= 0 and grid[r][b - 1] == -1:
                        b -= 1
                    else:
                        b = -1
                        break 

            ans.append(b)

        return ans 
