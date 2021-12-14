'''
Approach: DFS

Success
Details 
Runtime: 312 ms, faster than 39.13% of Python online submissions for Range Sum of BST.
Memory Usage: 29.7 MB, less than 61.85% of Python online submissions for Range Sum of BST.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        
        range_sum = 0
        if L <= root.val <= R:
            range_sum += root.val
        if root.left:
            range_sum += self.rangeSumBST(root.left, L, R)
        if root.right:
            range_sum += self.rangeSumBST(root.right, L, R)
        
        return range_sum

'''
DFS

Runtime: 204 ms, faster than 80.68% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.1 MB, less than 97.47% of Python3 online submissions for Range Sum of BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = [0]
        def helper(node):
            if not node:
                return
            if low <= node.val <= high:
                range_sum[0] += node.val
                helper(node.left)
                helper(node.right)
            if node.val < low:
                helper(node.right)
            if node.val > high:
                helper(node.left)
        
        helper(root)
        return range_sum[0]
        
'''
DFS

Runtime: 208 ms, faster than 71.98% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.2 MB, less than 85.71% of Python3 online submissions for Range Sum of BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = [0]
        def helper(node):
            if not node:
                return
            if low <= node.val <= high:
                range_sum[0] += node.val
            if node.val >= low:
                helper(node.left)
            if node.val <= high:
                helper(node.right)
        
        helper(root)
        return range_sum[0]

'''
Runtime: 208 ms, faster than 71.98% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.3 MB, less than 59.19% of Python3 online submissions for Range Sum of BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        range_sum = 0
        if low <= root.val <= high:
            range_sum += root.val
        if root.val >= low:
            range_sum += self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            range_sum += self.rangeSumBST(root.right, low, high)
        return range_sum      


'''
BFS

Runtime: 208 ms, faster than 71.98% of Python3 online submissions for Range Sum of BST.
Memory Usage: 22.5 MB, less than 5.88% of Python3 online submissions for Range Sum of BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        range_sum = 0
        q = deque([root])
        while q:
            node = q.popleft()
            if low <= node.val <= high:
                range_sum += node.val
            if node.val >= low and node.left:
                q.append(node.left)
            if node.val <= high and node.right:
                q.append(node.right)
        
        return range_sum

