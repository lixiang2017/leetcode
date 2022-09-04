'''
T: O(3MN), S: O(M+N)

执行用时：56 ms, 在所有 Python3 提交中击败了30.32% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了69.68% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # sum for row and column
        row_sum = [sum(row) for row in mat]
        m, n = len(mat), len(mat[0])
        col_sum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    ans += 1
        return ans 


'''
T: O(2MN), S: O(N)

执行用时：40 ms, 在所有 Python3 提交中击败了89.03% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了74.19% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        col_sum = [sum(mat[i][j] for i in range(m)) for j in range(n)]
        ans = 0
        for i, row in enumerate(mat):
            if sum(row) != 1:
                continue 
            for j, x in enumerate(row):
                if 1 != x or col_sum[j] != 1:
                    continue 
                ans += 1
        return ans 
