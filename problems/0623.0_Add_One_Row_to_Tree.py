'''
BFS

Runtime: 125 ms, faster than 13.33% of Python3 online submissions for Add One Row to Tree.
Memory Usage: 16.7 MB, less than 69.24% of Python3 online submissions for Add One Row to Tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        q = [root] if root else []
        d = 1   
        while q:

            if d + 1 == depth:
                for node in q:
                    node.left = TreeNode(val, node.left)
                    node.right = TreeNode(val, None, node.right)
                break 
            else:
                q = [child for node in q for child in [node.left, node.right] if child]
            d +=1 
        
        return root 
