'''
执行用时：40 ms, 在所有 Python3 提交中击败了29.72% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了68.06% 的用户
通过测试用例：14 / 14
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows - 1):
            last_row = [0] + ans[-1][:] + [0]
            new_row = []
            for j in range(len(last_row) - 1):
                new_row.append(last_row[j] + last_row[j + 1])
            ans.append(new_row)

        return ans 
        