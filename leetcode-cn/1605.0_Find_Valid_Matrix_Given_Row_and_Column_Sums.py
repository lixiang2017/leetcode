'''
Greedy
T: O(M+N)
S: O(1)

执行用时：64 ms, 在所有 Python3 提交中击败了92.42% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了48.48% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        mat = [[0] * n for _ in range(m)]
        i = j = 0
        while i < m and j < n:
            rs, cs = rowSum[i], colSum[j]
            if rs < cs:
                mat[i][j] = rs 
                colSum[j] -= rs 
                i += 1
            else:
                mat[i][j] = cs 
                rowSum[i] -= cs
                j += 1
        return mat

