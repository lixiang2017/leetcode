'''
approach: Math
C(n, i) = C(n, i - i) * (n - i + 1) / i
Time: O(N / 2) = O(N)
Space: O(N)

ref:
https://leetcode-cn.com/problems/pascals-triangle-ii/solution/yang-hui-san-jiao-ii-by-leetcode-solutio-shuk/
https://leetcode-cn.com/problems/pascals-triangle-ii/solution/yang-hui-san-jiao-ii-by-yxiaojian-a4z8/
https://leetcode-cn.com/problems/pascals-triangle-ii/solution/zu-he-de-di-tui-by-psyduck-w-ipst/


执行结果：通过
显示详情
执行用时：16 ms, 在所有 Python 提交中击败了79.69%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了55.63%的用户
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)
        for i in range(1, rowIndex / 2 + 1):
            row[i] = row[rowIndex - i] = row[i - 1] * (rowIndex - i + 1) / i

        return row
