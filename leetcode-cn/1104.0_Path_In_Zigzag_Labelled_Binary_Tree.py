'''
Iteration
Time: O(logN)
Space: O(1)

满二叉树的节点总数、每一层的节点数，跟指数函数均有等式关系。(等比数列的性质)
total_nodes = (2 ^ row) - 1
current_row_nodes = 2 ^ (row - 1))
1、先找到对应label的最大行row，再找最大行里label从左向右排第几个last_ith。last_ith的值跟row的奇偶性有关，要分情况计算。
2、再递推上层，上上层，上上上层... 也就是label对应的父节点，祖父节点，祖祖父节点... 每个父节点在当前行从左向右排第几个
除以2即可，但是注意奇数问题，所以要先加1，所以是
last_ith = (last_ith + 1) // 2
3、再根据last_ith计算出每行实际对应的数字。
4、最后列表倒置即可。

执行用时：12 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了57.81%的用户
'''
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        row = total = 0
        while total < label:
            row += 1
            total = (1 << row) - 1
        # last row i-th, from left to right
        if row % 2:
            # from left to right
            last_ith = label - ((1 << (row - 1)) - 1)
        else:
            # from left to right
            last_ith = ((1 << row) - 1) - label + 1
        ans = [label]
        while row > 1:
            last_ith = (last_ith + 1) // 2
            row -= 1
            if row % 2: # odd
                ans.append((1 << (row - 1)) - 1 + last_ith)
            else: # even
                # (1 << row) - 1 - last_ith + 1 = (1 << row) - last_ith
                ans.append((1 << row) - last_ith)
        return ans[:: -1]
