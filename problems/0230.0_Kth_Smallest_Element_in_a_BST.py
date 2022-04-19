'''
T: O(k)
S: O(1)

Runtime: 61 ms, faster than 69.02% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.1 MB, less than 48.12% of Python3 online submissions for Kth Smallest Element in a BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        ans = -1
        it = inorder(root)
        for _ in range(k):
            ans = next(it, None)
        return ans 
                

'''
DFS

Runtime: 60 ms, faster than 72.27% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 18.1 MB, less than 15.27% of Python3 online submissions for Kth Smallest Element in a BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = lambda node: count(node.left) + 1 + count(node.right) if node else 0
        
        left_cnt = count(root.left)
        if left_cnt == k - 1:
            return root.val
        elif left_cnt > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - left_cnt)
        

'''
@lru_cache(None)

Runtime: 55 ms, faster than 82.59% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.4 MB, less than 15.27% of Python3 online submissions for Kth Smallest Element in a BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        @lru_cache(None)
        def count(node):
            if not node: return 0
            return count(node.left) + 1 + count(node.right)
        
        left_cnt = count(root.left)
        if left_cnt == k - 1:
            return root.val
        elif left_cnt > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - left_cnt)
        

'''
@cache

Runtime: 48 ms, faster than 95.55% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.5 MB, less than 15.27% of Python3 online submissions for Kth Smallest Element in a BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        @cache
        def count(node):
            if not node: return 0
            return count(node.left) + 1 + count(node.right)
        
        left_cnt = count(root.left)
        if left_cnt == k - 1:
            return root.val
        elif left_cnt > k - 1:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - 1 - left_cnt)
        
        






