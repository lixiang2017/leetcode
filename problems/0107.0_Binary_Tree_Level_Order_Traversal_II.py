'''
Success
Details 
Runtime: 24 ms, faster than 62.77% of Python online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13.7 MB, less than 56.81% of Python online submissions for Binary Tree Level Order Traversal II.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        levels = []
        level = 0
        levels.append([root.val])  # level = 0
        # queue = deque([root, level], )  # Wrong
        queue = deque()
        queue.append([root, level])
        while queue:
            one_level = []
            node, level = queue.popleft()
            level += 1 
            if node.left:
                queue.append([node.left, level])
                one_level.append(node.left.val)
            if node.right:
                queue.append([node.right , level])
                one_level.append(node.right.val)
                
            if one_level:   # remove empty level
                if len(levels) > level:
                    print 'level: ', level
                    levels[level].extend(one_level)
                else:
                    levels.append(one_level)
        
        return levels[:: -1]
            
        
        