'''
You are here!
Your runtime beats 85.38 % of python submissions.
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
        def postorder(node):
            return postorder(node.left) + postorder(node.right) + [node.val] if node else []
        serialize_data = ' '.join(map(str, postorder(root)))
        # print 'serialize_data: ', serialize_data  # Output Limit Exceeded 
        return serialize_data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            # print 'data: ', data   # Output Limit Exceeded 
            # if not data:  # Wrong Answer  # always construct right-subtree
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            val = data.pop()
            root = TreeNode(val)
            # print 'root: ', root
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
            
        data = [int(x) for x in data.split() if x]
        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans