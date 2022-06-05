'''
执行用时：44 ms, 在所有 Python3 提交中击败了69.29% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了84.07% 的用户
通过测试用例：44 / 44
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        total = [[float('inf')] * n for _ in range(2)]
        total[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i + 1):
                if j == 0:
                    total[i & 1][j] = total[(i - 1) & 1][j] + triangle[i][j]
                else:
                    total[i & 1][j] =  triangle[i][j] + \
                        min(total[(i - 1) & 1][j - 1], total[(i - 1) & 1][j])

        return min(total[(n - 1) & 1])

