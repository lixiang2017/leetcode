'''
You are here!
Your runtime beats 29.62 % of python3 submissions.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self._hasnext = None
        self.iter = self.inorder(self.root)        

    def inorder(self, node):
        if not node:
            return None
        yield from self.inorder(node.left)
        yield node.val
        yield from self.inorder(node.right)
        
    def next(self) -> int:
        if self._hasnext:
            result = self._thenext 
        else:
            result = next(self.iter)
        self._hasnext = None
        return result
    
    def hasNext(self) -> bool:
        if self._hasnext is None:
            try: self._thenext = next(self.iter)
            except StopIteration: self._hasnext = None
            else: self._hasnext = True
        return self._hasnext
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
