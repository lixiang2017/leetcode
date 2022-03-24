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
