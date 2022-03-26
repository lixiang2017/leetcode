'''
simulation
T: O(9 * M * N)
S: O(1)

执行用时：260 ms, 在所有 Python3 提交中击败了78.81% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了76.42% 的用户
通过测试用例：203 / 203
'''
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        smooth = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s, cnt = 0, 0
                for ii in [i - 1, i, i + 1]:
                    for jj in [j - 1, j, j + 1]:
                        if 0 <= ii < m and 0 <= jj < n:
                            cnt += 1
                            s += img[ii][jj]
                smooth[i][j] = s // cnt 

        return smooth 


'''
二维prefix sum

执行用时：256 ms, 在所有 Python3 提交中击败了78.70% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了5.32% 的用户
通过测试用例：203 / 203
'''
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        smooth = [[0] * n for _ in range(m)]
        presum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                # img[i][j] -> presum[i + 1][j + 1]
                presum[i + 1][j + 1] = presum[i + 1][j] + presum[i][j + 1] + img[i][j] - presum[i][j]    

        for i in range(m):
            for j in range(n):
                left = max(j - 1, 0)
                right = min(j + 1, n - 1)
                up = max(i - 1, 0)
                down = min(i + 1, m - 1)
                s = presum[down + 1][right + 1] - presum[down + 1][left] - presum[up][right + 1] + presum[up][left]
                cnt = (down - up + 1) * (right - left + 1)
                smooth[i][j] = s // cnt 

        return smooth



