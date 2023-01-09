'''
DFS

Runtime: 34 ms, faster than 77.91% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 57.18% of Python3 online submissions for Binary Tree Preorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

'''
iteration

Runtime: 25 ms, faster than 97.47% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.9 MB, less than 57.18% of Python3 online submissions for Binary Tree Preorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans 
        

