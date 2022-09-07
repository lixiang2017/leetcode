'''
DFS

Runtime: 108 ms, faster than 19.23% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 16.5 MB, less than 10.51% of Python3 online submissions for Construct String from Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def preorder(node, direction):
            if not node:
                if 'L' == direction:
                    return '()'
                else:
                    return ''
                
            if not node.left and not node.right:
                if 'M' == direction:
                    return str(node.val)
                else:
                    return '(' + str(node.val) + ')'
            
            left_str = preorder(node.left, 'L') 
            right_str = preorder(node.right, 'R') 
            root_str = str(node.val) 
            all_str = root_str + left_str + right_str
            ans = all_str if direction == 'M' else '(' + all_str + ')'
            return ans 

        return preorder(root, 'M')
