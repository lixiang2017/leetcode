'''
Level Order,T:O(N),S:O(N)

执行用时：172 ms, 在所有 Python3 提交中击败了29.98% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了16.03% 的用户
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
            return ''
        level = ''
        q = [root]
        while q:
            node = q.pop(0)
            if not node:
                level += 'None,'
                continue
            level += str(node.val) + ','
            q.append(node.left)
            q.append(node.right)
        return level

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = iter(data.split(','))
        root = TreeNode(next(data))
        q = [root]
        while q:
            node = q.pop(0)
            left, right = next(data), next(data)
            if left != 'None':
                node.left = TreeNode(left)
                q.append(node.left)
            if right != 'None':
                node.right = TreeNode(right)
                q.append(node.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

