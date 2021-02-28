'''
approach: DFS
Time: O(N)
Space: O(N)

执行用时：52 ms, 在所有 Python 提交中击败了18.40%的用户
内存消耗：16 MB, 在所有 Python 提交中击败了34.43%的用户
'''


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        post = []
        for child in root.children:
            childPost = self.postorder(child)
            post += childPost
        post += [root.val]

        return post
