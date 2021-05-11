'''
approach: DFS + Sort + OrderedDict
Time: O(N + NlogN + N) = O(NlogN)
Space: O(N)

You are here!
Your runtime beats 99.85 % of python submissions.
You are here!
Your memory usage beats 86.09 % of python submissions.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import OrderedDict

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        nodes = []
        def dfs(node, x, y):
            if not node: return
            nodes.append([x, y, node.val])
            dfs(node.left, x - 1, y + 1)   # use y + 1 instead of y - 1 to avoid compare function in following sort
            dfs(node.right, x + 1, y + 1)
           
        dfs(root, 0, 0)
        nodes.sort()
        vertical = OrderedDict()
        for x, y, val in nodes:
            if x in vertical:
                vertical[x].append(val)
            else:
                vertical[x] = [val]
        
        # print 'vertical: ', vertical
        return vertical.values()

'''
vertical:  OrderedDict([(-1, [9]), (0, [3, 15]), (1, [20]), (2, [7])])    
'''
