'''
执行用时：3040 ms, 在所有 Python3 提交中击败了5.03% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了27.87% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        up = True
        for s in range(m + n):  # s = i + j
            if up:
                for i in range(min(m - 1, s), -1, -1):
                    j = s - i 
                    if 0 <= j < n:
                        ans.append(mat[i][j])
                up = False 
            else:
                for i in range(min(m, s + 1)):
                    j = s - i
                    if 0 <= j < n:
                        ans.append(mat[i][j])
                up = True
        return ans 

'''
break, 减少没必要的搜索

执行用时：68 ms, 在所有 Python3 提交中击败了33.31% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了57.51% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        up = True
        for s in range(m + n):  # s = i + j
            if up:
                for i in range(min(m - 1, s), -1, -1):
                    j = s - i 
                    if 0 <= j < n:
                        ans.append(mat[i][j])
                    else:
                        break
                up = False 
            else:
                for i in range(max(0, s-(n-1)) , min(m, s + 1)):
                    j = s - i
                    ans.append(mat[i][j])
                up = True
        return ans 


'''
remove break

执行用时：56 ms, 在所有 Python3 提交中击败了74.92% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了24.54% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        up = True
        for s in range(m + n):  # s = i + j
            if up:
                for i in range(min(m - 1, s), max(-1, s-(n-1)-1), -1):
                    j = s - i 
                    ans.append(mat[i][j])
                up = False 
            else:
                for i in range(max(0, s-(n-1)) , min(m, s + 1)):
                    j = s - i
                    ans.append(mat[i][j])
                up = True
        return ans 





