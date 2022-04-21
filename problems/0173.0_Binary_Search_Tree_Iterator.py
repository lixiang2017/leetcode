'''
Runtime: 107 ms, faster than 39.74% of Python3 online submissions for Binary Search Tree Iterator.
Memory Usage: 20.5 MB, less than 35.61% of Python3 online submissions for Binary Search Tree Iterator.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.it = iter(self.inorder(root))
        self.x = None
        
    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.val 
            yield from self.inorder(node.right)
        
    def next(self) -> int:
        x = self.x
        if x is None:
            x = next(self.it, None)
        self.x = None
        return x 

    def hasNext(self) -> bool:
        if self.x is None:
            self.x = next(self.it, None)
        return self.x is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


