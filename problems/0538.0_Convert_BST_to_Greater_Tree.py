'''
postfix sum / dfs
T: O(N)
S: O(logN)

Runtime: 88 ms, faster than 83.72% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 16.6 MB, less than 97.31% of Python3 online submissions for Convert BST to Greater Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        postsum = 0
        def dfs(node):
            nonlocal postsum
            if not node:
                return 
            dfs(node.right)
            postsum += node.val
            node.val = postsum
            dfs(node.left)
        
        dfs(root)
        return root


'''
postfix sum / dfs
T: O(N)
S: O(logN)

Runtime: 88 ms, faster than 83.72% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 16.7 MB, less than 77.23% of Python3 online submissions for Convert BST to Greater Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        postsum = 0
        def dfs(node):
            nonlocal postsum
            if not node:
                return 
            dfs(node.right)
            postsum += node.val
            node.val = postsum
            dfs(node.left)
        
        dfs(root)
        return root

'''
pass by reference / dfs
T: O(N)
S: O(logN)

Runtime: 86 ms, faster than 84.58% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 16.7 MB, less than 77.23% of Python3 online submissions for Convert BST to Greater Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, s):
            if not node:
                return 
            dfs(node.right, s)
            s[0] += node.val
            node.val = s[0]
            dfs(node.left, s)
        
        dfs(root, [0])
        return root


'''
iteration

Runtime: 75 ms, faster than 98.41% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 16.7 MB, less than 53.49% of Python3 online submissions for Convert BST to Greater Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        node = root
        postsum = 0
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            postsum += node.val
            node.val = postsum
            node = node.left
        
        return root



