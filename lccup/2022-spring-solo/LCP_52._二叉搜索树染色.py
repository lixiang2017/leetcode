'''
逆向思维，think in a reversed way
不一定用 线段树+懒标记
https://leetcode-cn.com/problems/QO5KpG/

执行用时：852 ms, 在所有 Python3 提交中击败了100.00%的用户
内存消耗：65.1 MB, 在所有 Python3 提交中击败了100.00%的用户
通过测试用例：
89 / 89
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        nums = list(inorder(root))
        ans = 0
        for t, x, y in ops[:: -1]:
            left = bisect_left(nums, x)
            right = bisect_right(nums, y)
            if t == 1:
                ans += right - left 
            nums[left: right] = []

        return ans
