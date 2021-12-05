'''
DFS

Runtime: 72 ms, faster than 19.77% of Python3 online submissions for House Robber III.
Memory Usage: 18.7 MB, less than 7.40% of Python3 online submissions for House Robber III.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node, amount, isRob):
            if not node:
                return 0
            if isRob:
                amount += node.val
            
            nl1 = nr1 = rl = rr = nl2 = nr2 = 0
            if isRob:
                # can not rob left or right child
                nl1 = dfs(node.left, 0, False)
                nr1 = dfs(node.right, 0, False)
            else:
                # can rob left or right child
                ## rob
                rl = dfs(node.left, 0, True)
                rr = dfs(node.right, 0, True)                
                # not rob
                nl2 = dfs(node.left, 0, False)
                nr2 = dfs(node.right, 0, False) 
                
            return amount + (
                max(
                    nl1 + nr1, rl + rr, rl + nr2, nl2 + rr, nl2 + nr2
                )
            )
        
        rob_root = dfs(root, 0, True)
        not_rob_root = dfs(root, 0, False)
        return max(rob_root, not_rob_root)

'''
Runtime: 64 ms, faster than 30.29% of Python3 online submissions for House Robber III.
Memory Usage: 18.1 MB, less than 14.54% of Python3 online submissions for House Robber III.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @cache
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        # rob 
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)
        # not rob
        val2 = self.rob(root.left) + self.rob(root.right)
    
        return max(val1, val2)
               
