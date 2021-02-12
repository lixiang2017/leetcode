'''
approach: Iteration / Dynamic Programming
Time: O(N^2)
Space: O(N^2)

执行结果：
通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了79.69%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了84.99%的用户
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rows = []
        rows.append([1])
        for i in range(34):
            full_row = [0] + rows[-1] + [0]
            size = len(full_row)
            new_row = []
            for j in range(size - 1):
                new_row.append(full_row[j] + full_row[j + 1])
            rows.append(new_row)

        return rows[rowIndex]


'''
approach: Iteration
Time: O(N^2)
Space: O(N)

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了29.36%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了49.67%的用户
'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            full_row = [0] + row + [0]
            size = len(full_row)
            new_row = []
            for j in range(size - 1):
                new_row.append(full_row[j] + full_row[j + 1])
            row = new_row

        return row
