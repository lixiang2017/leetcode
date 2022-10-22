'''
DFS

执行用时：112 ms, 在所有 Python3 提交中击败了6.92% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了6.71% 的用户
通过测试用例：182 / 182
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None 
        return TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0),
            self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None),
            self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
            )
      
        
'''
执行用时：64 ms, 在所有 Python3 提交中击败了79.48% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了51.94% 的用户
通过测试用例：182 / 182
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 and t2:
            t1.val += t2.val 
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1 
        return t1 or t2 
