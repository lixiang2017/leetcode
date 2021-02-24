'''
approach: DFS / Recursion
Time: O(N), where N is the number of nodes in the given tree.
Space: O(Height), where Height is the max Depth of the given tree.

执行用时：32 ms, 在所有 Python 提交中击败了52.52%的用户
内存消耗：15.5 MB, 在所有 Python 提交中击败了84.45%的用户
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1
        

'''
approach: BFS / Iteration
Time: O(N), where N is the number of nodes in the given tree.
Space: O(L), where L the the maximum number of nodes in a level.

执行结果：
通过
显示详情
执行用时：24 ms, 在所有 Python 提交中击败了90.45%的用户
内存消耗：15.5 MB, 在所有 Python 提交中击败了92.36%的用户
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [(root, 1)]   # (node, level)
        depth = 1
        while q:
            node, level = q.pop(0)
            depth = max(depth, level)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return depth

'''
approach: BFS / Iteration
Time: O(N), where N is the number of nodes in the given tree.
Space: O(L), where L the the maximum number of nodes in a level.

执行用时：24 ms, 在所有 Python 提交中击败了90.45%的用户
内存消耗：15.6 MB, 在所有 Python 提交中击败了58.66%的用户
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            next_q = []
            for node in q:
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            depth += 1
            q = next_q
        return depth
