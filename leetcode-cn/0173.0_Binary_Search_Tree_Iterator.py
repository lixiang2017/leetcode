'''
执行用时：120 ms, 在所有 Python3 提交中击败了6.27%的用户
内存消耗：20.8 MB, 在所有 Python3 提交中击败了71.72%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        def inOrder(node):
            if not node:
                return None
            yield from inOrder(node.left)
            yield node.val
            yield from inOrder(node.right)
        self.in_order = []
        for one in inOrder(root):
            self.in_order.append(one)
        self.ptr = 0
        self.N = len(self.in_order)

    def next(self) -> int:
        val = self.in_order[self.ptr]
        self.ptr += 1
        return val

    def hasNext(self) -> bool:
        return self.ptr < self.N



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
