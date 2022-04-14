'''
recursion
T: O(logN)
S: O(N)

Runtime: 83 ms, faster than 79.14% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 16.6 MB, less than 28.83% of Python3 online submissions for Search in a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
        

'''
iteration
T: O(logN)
S: O(1)

Runtime: 79 ms, faster than 86.12% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 16.4 MB, less than 74.05% of Python3 online submissions for Search in a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            elif node.val < val:
                if node.right:
                    q.append(node.right)
            else:
                if node.left:
                    q.append(node.left)
        return None
        
