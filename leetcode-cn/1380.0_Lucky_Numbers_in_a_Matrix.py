'''
T: O(2MN), S:O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了77.10% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了9.81% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            min_idx, minx = 0, row[0]
            for j, x in enumerate(row):
                if x < minx:
                    minx = x 
                    min_idx = j

            isLucky = True
            for ii in range(m):
                if matrix[ii][min_idx] > minx:
                    isLucky = False
                    break
            if isLucky:
                ans.append(minx)
                
        return ans 

'''
执行用时：44 ms, 在所有 Python3 提交中击败了58.22% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了53.99% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowmin = [min(row) for row in matrix]
        colmax = [max(col) for col in zip(*matrix)]
        return list(set(rowmin) & set(colmax))


'''
执行用时：40 ms, 在所有 Python3 提交中击败了77.00% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了71.83% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowmin = [min(row) for row in matrix]
        colmax = [max(col) for col in zip(*matrix)]
        return [x for x in rowmin if x in colmax]

