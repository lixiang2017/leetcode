'''
approach: DFS

执行用时：3104 ms, 在所有 Python 提交中击败了5.07%的用户
内存消耗：406.9 MB, 在所有 Python 提交中击败了5.09%的用户
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestorP = self.ancestor(root, [], p)
        ancestorQ = self.ancestor(root, [], q)
        lenP, lenQ = len(ancestorP), len(ancestorQ)
        if lenP > lenQ:
            ancestorP, ancestorQ = ancestorQ, ancestorP
            lenP, lenQ = lenQ, lenP
        for i in range(lenP):
            if ancestorP[i] != ancestorQ[i]:
                return ancestorP[i - 1]
        return ancestorP[-1]
            
    
    def ancestor(self, root, path, node):
        if not root:
            return []
        
        if root == node:
            return path + [node]
        
        left = self.ancestor(root.left, path + [root], node)
        right = self.ancestor(root.right, path + [root], node)
        return left or right
        