'''
https://leetcode-cn.com/problems/SNJvJP/
math

执行用时：40 ms, 在所有 Python3 提交中击败了44.72% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了32.16% 的用户
'''

class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        x, y = xPos, yPos
        MOD = 9
        # min, 从0开始第几圈
        m = min(xPos, yPos, num - 1 - xPos, num - 1 -yPos)
        #print('m: ', m)
        # (num-1)*4, (num-3)*4, (num-5)*4....(num-(2*m-1)*4)
        total = 4 * m * (num - m)
        #print('total:', total)
        edge = num - 2 * m - 1
        #print('edge: ', edge)
        # top
        if xPos == m:
            total += y - m            
        # right
        elif num - 1 - yPos == m:
            total += edge + x - m
        # bottom
        elif num - 1 - xPos == m:
            total += edge * 2 + edge - (y - m)
        # left
        elif yPos == m:
            total += edge * 3 + edge - (x - m)

        return total % MOD + 1

