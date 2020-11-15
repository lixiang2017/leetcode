'''
BFS

You are here!
Your runtime beats 98.94 % of python submissions.
'''



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        range_sum = 0
        st = [root]
        while st:
            node = st.pop()
            if not node:
                continue
            if low <= node.val <= high:
                range_sum += node.val
            if node.val > low:
                st.append(node.left)
            if node.val < high:
                st.append(node.right)
        
        return range_sum
