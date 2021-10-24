'''
T: O(M+N), S: O(1)

执行用时：148 ms, 在所有 Python3 提交中击败了84.10% 的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了49.99% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        i, j = M - 1, 0
        while i >= 0 and j < N:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
                
        return False
