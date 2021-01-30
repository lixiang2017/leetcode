'''
aproach: BFS + Sort 
Time: O(N + NlogN + N) = O(NlogN), N is the number of nodes
Space: O(N + N + N + N) = O(N)

You are here!
Your runtime beats 14.66 % of python submissions.
You are here!
Your memory usage beats 64.58 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        nodes = [(0, 0, root.val)]  # (x, y, val)
        q = [(0, 0, root.val, root)]  # (x, y, val, pointer)
        while q:
            x, y, val, head = q.pop(0)
            if head.left:
                q.append((x - 1, y - 1, head.left.val, head.left))
                nodes.append((x - 1, y - 1, head.left.val))
            if head.right:
                q.append((x + 1, y - 1, head.right.val, head.right))
                nodes.append((x + 1, y - 1, head.right.val))
        
        nodes.sort(key=lambda t: (t[0], -t[1], t[2]))
        # print nodes
        
        vertical = []
        pre_x = nodes[0][0]
        column = []
        for x, y, val in nodes:
            if x == pre_x:
                column.append(val)
            else:
                vertical.append(column)
                column = [val]
                pre_x = x
        vertical.append(column)
        
        return vertical
        