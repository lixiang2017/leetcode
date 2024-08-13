'''
DFS + BFS

执行用时：116 ms, 在所有 Python3 提交中击败了70.98% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了93.44% 的用户
通过测试用例：182 / 182
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True 

        def identical(root1, root2):
            if not root1 and not root2:
                return True 
            elif root1 and root2:
                return root1.val == root2.val and identical(root1.left, root2.left) and identical(root1.right, root2.right)
            else:
                return False 
        
        q = [root]
        while q:
            next_q = []
            for node in q:
                if identical(node, subRoot):
                    return True 
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            q = next_q
            
        return False 




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if not r1 and not r2:
            return True
        if (not r1 and r2) or (r1 and not r2) or (r1.val != r2.val):
            return False
        return self.same(r1.left, r2.left) and self.same(r1.right, r2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.same(root, subRoot):
            return True
        return (root.left is not None and self.isSubtree(root.left, subRoot)) or\
            (root.right is not None and self.isSubtree(root.right, subRoot))



            