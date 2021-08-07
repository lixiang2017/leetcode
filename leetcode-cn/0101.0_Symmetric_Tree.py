'''
DFS,T:O(N),S:O(N)

执行用时：24 ms, 在所有 Python3 提交中击败了99.48% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.05% 的用户
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def compare(node1, node2):
            if (not node1 and not node2):
                return True
            if (not node1 and node2) or (node1 and not node2) or (node1.val != node2.val):
                return False
            return compare(node1.left, node2.right) and compare(node1.right, node2.left)
        
        return compare(root.left, root.right)

'''
BFS,T:O(N),S:O(N)

执行用时：48 ms, 在所有 Python3 提交中击败了25.97% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了20.89% 的用户
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque([root, root])
        while q:
            u, v = q.popleft(), q.popleft()
            if not u and not v:
                continue
            if (not u and v) or (u and not v) or (u.val != v.val):
                return False
            q.append(u.left)
            q.append(v.right)
            #
            q.append(u.right)
            q.append(v.left)

        return True

