'''
You are here!
Your runtime beats 78.74 % of python3 submissions.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = []
        self.ptr = -1
        for val in self.inorder(root):
            self.vals.append(val)
        

    def inorder(self, node):
        if not node:
            return None
        yield from self.inorder(node.left)
        yield node.val
        yield from self.inorder(node.right)
        

    def next(self):
        """
        :rtype: int
        """
        self.ptr += 1
        return self.vals[self.ptr]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.ptr != len(self.vals) - 1:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

