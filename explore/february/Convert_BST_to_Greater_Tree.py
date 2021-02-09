'''
approach: DFS + PostSum
Time: O(N + N + N) = O(N)
Space: O(N + N) = O(N)

You are here!
Your runtime beats 6.98 % of python submissions.
You are here!
Your memory usage beats 41.28 % of python submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        
        in_order = []
        post_sum = []
        in_order = self.inOrder(root)
        for val in in_order[:: -1]:
            post_sum.insert(0, val + post_sum[0] if post_sum else val)
        self.setValue(root, in_order, post_sum)
        return root
        
    def inOrder(self, node):
        in_order = []
        if not node: return []
        left_part = self.inOrder(node.left)
        right_part = self.inOrder(node.right)
        return left_part + [node.val] + right_part
        
    def setValue(self, node, inOrder, postSum):
        if not node: return
        node.val = postSum[inOrder.index(node.val)]
        self.setValue(node.left, inOrder, postSum)
        self.setValue(node.right, inOrder, postSum)





'''
Success
Details 
Runtime: 68 ms, faster than 91.28% of Python online submissions for Convert BST to Greater Tree.
Memory Usage: 17.6 MB, less than 98.26% of Python online submissions for Convert BST to Greater Tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(root, s):
            if root:
                inorder(root.right, s)
                root.val += s[0]
                s[0] = root.val
                inorder(root.left, s)
        inorder(root, [0])
        return root


'''
approach: DFS(right child -> node -> left child)
Time: O(N)
Space: O(N)

Success
Details 
Runtime: 80 ms, faster than 37.21% of Python online submissions for Convert BST to Greater Tree.
Memory Usage: 17.8 MB, less than 65.70% of Python online submissions for Convert BST to Greater Tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.total = 0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        return root
    

'''
approach: Iterative DFS - inorder
Success
Details 
Runtime: 68 ms, faster than 91.28% of Python online submissions for Convert BST to Greater Tree.
Memory Usage: 17.9 MB, less than 41.28% of Python online submissions for Convert BST to Greater Tree.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        stack = []
        node = root
        total = 0
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
                
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        return root
            
       
        