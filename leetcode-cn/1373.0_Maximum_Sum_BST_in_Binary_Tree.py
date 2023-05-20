'''
执行用时：340 ms, 在所有 Python3 提交中击败了50.37% 的用户
内存消耗：71 MB, 在所有 Python3 提交中击败了9.63% 的用户
通过测试用例：58 / 58
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans 
            if not node:
                return True, 0, inf, -inf
            
            isLeftBST, _sumLeft, leftMin, leftMax = dfs(node.left)
            isRgihtBST, _sumRight, rightMin, rightMax = dfs(node.right)

            isBST = isLeftBST and isRgihtBST and leftMax < node.val < rightMin
            _sum = _sumLeft + node.val + _sumRight
            _max = max(leftMax, rightMax, node.val)
            _min = min(leftMin, rightMin, node.val)
            if isBST:
                ans = max(ans, _sum)
            return isBST, _sum, _min, _max
        
        dfs(root)
        return ans 
        