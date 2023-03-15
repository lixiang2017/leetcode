'''
idx == seq
BFS

Runtime: 27 ms, faster than 99.14% of Python3 online submissions for Check Completeness of a Binary Tree.
Memory Usage: 13.9 MB, less than 18.83% of Python3 online submissions for Check Completeness of a Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = [(root, 1)] if root else []
        seq = 1
        
        while q:
            next_q = []
            for node, idx in q:
                if idx != seq:
                    return False
                seq += 1
                if node.left:
                    next_q.append((node.left, 2 * idx))
                if node.right:
                    next_q.append((node.right, 2 * idx + 1))
            q = next_q
        return True


'''
BFS

Runtime: 38 ms, faster than 56.30% of Python3 online submissions for Check Completeness of a Binary Tree.
Memory Usage: 13.9 MB, less than 18.83% of Python3 online submissions for Check Completeness of a Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if not root:
                return 0
            l = getHeight(root.left)
            r = getHeight(root.right)
            return max(l, r) + 1
        
        h = getHeight(root)
        
        q = [root] if root else []
        cur_h = 0
        while q:
            next_q = []
            if len(q) != (1 << cur_h):
                return False
            for i, node in enumerate(q):
                if node.left is None and node.right is not None:
                    return False
                if i != len(q) - 1 and node.right is None and q[i + 1].left is not None:
                    return False
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            cur_h += 1
            q = next_q
            if cur_h == h - 1:
                break
        return True
    
'''
[1,2,3,4,5,6]
[1,2,3,4,5,null,7]
[1,2,3,5]
[1,2,3,5,null,7,8]
[1,2,3,null,6,7,8]
'''
