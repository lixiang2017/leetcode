'''
from up-right to bottom-left
T: O(M + N)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了17.63%的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了45.87%的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0]) if matrix else 0
        i, j = 0, m - 1
        while i < n and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False


'''
from bottom-left to up-right
T: O(M + N)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了34.66% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了43.89% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0]) if matrix else 0
        i, j = n - 1, 0
        while i >= 0 and j < m:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

'''
brute force
T: O(MN)
S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了34.66% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了45.27% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for x in row:
                if x == target:
                    return True
        return False

'''
binary search every row
T: O(NlogM)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了58.27% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了26.42% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0]) if matrix else 0
        for row in matrix:
            idx = bisect_left(row, target)
            if idx < m and row[idx] == target:
                return True
        return False


'''
binary search every column
T: O(MlogN)
S: O(1)

执行用时：52 ms, 在所有 Python3 提交中击败了8.55% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了63.71% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        for col in zip(*matrix):
            idx = bisect_left(col, target)
            if idx < n and col[idx] == target:
                return True
        return False


'''
binary search by the longer one (row/column)
T: O( min(N,M)*log(max(N,M)) )
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了58.27% 的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了12.85% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0]) if matrix else 0
        if n < m:
            for row in matrix:
                idx = bisect_left(row, target)
                if idx < m and row[idx] == target:
                    return True
        else:
            for col in zip(*matrix):
                idx = bisect_left(col, target)
                if idx < n and col[idx] == target:
                    return True
        return False

'''
binary search by the longer one (row/column)
T: O( min(N,M)*log(max(N,M)) )
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了58.27% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了35.85% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0]) if matrix else 0
        if n > m:
            matrix = zip(*matrix)
    
        for longer in matrix:
            idx = bisect_left(longer, target)
            if idx < max(n, m) and longer[idx] == target:
                return True
        return False


'''
brute force
执行用时：48 ms, 在所有 Python3 提交中击败了17.63% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了31.53% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)


'''
divide and conquer, cut to four parts + binary search

执行用时：48 ms, 在所有 Python3 提交中击败了17.63% 的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了5.10% 的用户
通过测试用例：129 / 129
'''
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0]) if matrix else 0

        def isExist(i1, j1, i2, j2):
            if i1 > i2 or j1 > j2:
                return False 
            if i1 == i2:
                # matrix[i1][j1: j2 + 1]
                lo, hi = j1, j2
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if matrix[i1][mid] == target:
                        return True
                    elif matrix[i1][mid] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                return False 
            elif j1 == j2:
                # matrix[i1: i2 + 1][j1]
                lo, hi = i1, i2
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if matrix[mid][j1] == target:
                        return True
                    elif matrix[mid][j1] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                return False

            #  cut to four parts
            midi, midj = (i1 + i2) // 2, (j1 + j2) // 2
            if matrix[midi][midj] == target:
                return True
            elif matrix[midi][midj] > target:
                return isExist(i1, j1, midi, midj) or \
                    isExist(i1, midj + 1, midi, j2) or \
                    isExist(midi + 1, j1, i2, midj)
            else:
                return isExist(midi + 1, midj + 1, i2, j2) or \
                    isExist(i1, midj + 1, midi, j2) or \
                    isExist(midi + 1, j1, i2, midj)
        return isExist(0, 0, n - 1, m - 1)




