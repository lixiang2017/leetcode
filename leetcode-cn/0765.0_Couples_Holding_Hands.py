'''
approach: Greedy
Time: O(N ^ 2)
Space: O(1)

ref:
https://leetcode-cn.com/problems/couples-holding-hands/solution/tan-xin-suan-fa-by-good_guy-c3ol/

执行结果：
通过
显示详情
执行用时：20 ms, 在所有 Python 提交中击败了73.68%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了68.42%的用户
'''


class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        swaps = 0
        size = len(row)
        for i in range(0, size, 2):
            need = row[i] ^ 1
            if need == row[i + 1]:
                continue
            # search for partner
            swaps += 1
            for j in range(i + 2, size):
                if row[j] == need:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    break
        return swaps
