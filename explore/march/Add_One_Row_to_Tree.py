'''
approach: BFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 91.55 % of python submissions.
You are here!
Your memory usage beats 81.69 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if 1 == d:
            return TreeNode(val=v, left=root)
        
        q = [(root, 1)]  #(node, depth)
        while q:
            next_level = []
            if d - 1 == q[0][1]:
                next_level = []
                for node, depth in q:
                    if node.left:
                        node.left = TreeNode(val=v, left=node.left)
                    else:
                        node.left = TreeNode(val=v, left=None)
                    if node.right:
                        node.right = TreeNode(val=v, right=node.right)
                    else:
                        node.right = TreeNode(val=v, right=None)
                break
            else:
                for node, depth in q:
                    if node.left:
                        next_level.append((node.left, depth + 1))
                    if node.right:
                        next_level.append((node.right, depth + 1))
                q = next_level
        
        return root



'''
approach: BFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 91.55 % of python submissions.
You are here!
Your memory usage beats 67.61 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if 1 == d:
            return TreeNode(val=v, left=root)
        
        q = [(root, 1)]  #(node, depth)
        while q:
            next_level = []
            if d - 1 == q[0][1]:
                next_level = []
                for node, depth in q:
                    node.left = TreeNode(val=v, left=node.left)
                    node.right = TreeNode(val=v, right=node.right)

                break
            else:
                for node, depth in q:
                    if node.left:
                        next_level.append((node.left, depth + 1))
                    if node.right:
                        next_level.append((node.right, depth + 1))
                q = next_level
        
        return root



'''
approach: DFS

You are here!
Your runtime beats 91.55 % of python submissions.
You are here!
Your memory usage beats 35.21 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if 1 == d:
            return TreeNode(val=v, left=root)
        
        self.dfs(root, 1, v, d)
        return root
        
    
    def dfs(self, node, depth, v, d):
        if not node:
            return
        
        if depth == d - 1:
            node.left = TreeNode(val=v, left=node.left)
            node.right = TreeNode(val=v, right=node.right)
            return 
        
        self.dfs(node.left, depth + 1, v, d)
        self.dfs(node.right, depth + 1, v, d)

