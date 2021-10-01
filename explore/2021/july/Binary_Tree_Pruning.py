'''
DFS

You are here!
Your runtime beats 6.84 % of python3 submissions.
You are here!
Your memory usage beats 57.39 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def helper(node: TreeNode):
            '''sum of self and children'''
            if not node:
                return 0
            
            if helper(node.left) == 0:
                node.left = None
            if helper(node.right) == 0:
                node.right = None

            return node.val + helper(node.left) + helper(node.right)

        helper(root)
        if root and root.val == 0 and not root.left and not root.right:
            return None
        else:
            return root

    
'''
Input: [0,null,0,0,0]
Output: [0]
Expected: []
'''


'''
DFS
You are here!
Your runtime beats 24.51 % of python3 submissions.
You are here!
Your memory usage beats 98.95 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(node: TreeNode):
            if not node:
                return 0
            left, right = prune(node.left), prune(node.right)
            if not left:
                node.left = None
            if not right:
                node.right = None    
            return node.val + left + right
        
        root_val = prune(root)
        return None if not root_val else root


'''
You are here!
Your runtime beats 63.61 % of python3 submissions.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root if root.left or root.right or root.val else None



'''
You are here!
Your runtime beats 63.61 % of python3 submissions.
You are here!
Your memory usage beats 82.45 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val:
            return None
        return root


'''

'''
'''
Recursion
Time: O(N), where N is ther number of nodes in the tree. We process each node once.
Space: O(N), the recursion call stack can be as large as the height H of the tree. 
In the worst case scenario, H = N, when the tree is skewed.

Runtime: 24 ms, faster than 95.94% of Python3 online submissions for Binary Tree Pruning.
Memory Usage: 14.4 MB, less than 22.72% of Python3 online submissions for Binary Tree Pruning.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def contains_one(node: TreeNode) -> bool:
            if not node:
                return False
            # Check if any node in the left subtree contains a 1.
            left_contains_one = contains_one(node.left)
            # Check if any node in the right subtree contains a 1.
            right_contains_one = contains_one(node.right)
            # If the left subtree does not contain a 1, prune the subtree.
            if not left_contains_one:
                node.left = None
            # If the right subtree does not contain a 1, prune the subtree.
            if not right_contains_one:
                node.right = None
            # Return True if the current node or its left or right subtree contains a 1.
            return node.val or left_contains_one or right_contains_one
    
        # Return the pruned tree if the tree contains a 1, otherwise return None.
        return root if contains_one(root) else None
