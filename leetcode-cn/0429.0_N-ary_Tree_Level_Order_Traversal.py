'''
approach: BFS
Time: O(N)
Space: O(N)

执行用时：44 ms, 在所有 Python 提交中击败了48.84%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了64.53%的用户
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        q = [root]
        level = []
        while q:
            current_level_values = []
            next_level = []
            for node in q:
                for child in node.children:
                    next_level.append(child)
                current_level_values.append(node.val)
            level.append(current_level_values)
            q = next_level

        return level
