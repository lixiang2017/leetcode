'''
Recursive
T: O(N)
S: O(logN)

Runtime: 140 ms, faster than 11.93% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.6 MB, less than 57.82% of Python3 online submissions for Count Complete Tree Nodes.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


'''
Recursive
T: O((logN)^2)
S: O(logN)

Runtime: 86 ms, faster than 58.58% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.5 MB, less than 84.58% of Python3 online submissions for Count Complete Tree Nodes.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        h = self.getHeight(root)
        if -1 == h:
            return 0
        rh = self.getHeight(root.right)
        if rh == h - 1:
            return (1 << h) + self.countNodes(root.right)
        else:
            return (1 << (h - 1)) + self.countNodes(root.left)

    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        return 1 + self.getHeight(node.left)



'''
Iterative
T: O((logN)^2)
S: O(logN)

Runtime: 64 ms, faster than 98.32% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.7 MB, less than 15.78% of Python3 online submissions for Count Complete Tree Nodes.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        h = self.getHeight(root)
        nodes = 0
        while root:
            rh = self.getHeight(root.right)
            if rh == h - 1:
                nodes += (1 << h)
                root = root.right
            else:
                nodes += (1 << (h - 1))
                root = root.left
            h -= 1
            
        return nodes 
        
    def getHeight(self, node: Optional[TreeNode]) -> int:
        h = -1
        while node:
            node = node.left
            h += 1
        return h



'''
Recursive
T: O((logN)^2)
S: O(logN)

ref:
https://leetcode.com/problems/count-complete-tree-nodes/discuss/61958/Concise-Java-solutions-O(log(n)2)

Runtime: 104 ms, faster than 35.24% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.6 MB, less than 57.82% of Python3 online submissions for Count Complete Tree Nodes.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = right = root
        h = 0
        while right:
            left = left.left
            right = right.right
            h += 1
        if not left:
            return (1 << h) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

