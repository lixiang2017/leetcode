'''
Pre Order + DFS
Time: O(N)
Space: O(N)

执行用时：124 ms, 在所有 Python3 提交中击败了86.05% 的用户
内存消耗：19.5 MB, 在所有 Python3 提交中击败了50.25% 的用户
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#,'
        pre = str(root.val) + ','
        pre += self.serialize(root.left)
        pre += self.serialize(root.right)
        return pre

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split(','))
        def helper():
            val = next(data)
            if val == '#':
                return 
            root = TreeNode(int(val))
            root.left = helper()
            root.right = helper()
            return root
        return helper()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
