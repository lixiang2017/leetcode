'''
You are here!
Your runtime beats 13.59 % of python3 submissions.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(node: TreeNode) -> List[int]:
            if not node:
                return []            
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        nums = inorder(root)
        l, r = 0, len(nums) - 1
        while l < r:
            t = nums[l] + nums[r]
            if k == t:
                return True
            elif k > t:
                l += 1
            else:
                r -= 1
        return False


'''
You are here!
Your runtime beats 68.75 % of python3 submissions.
You are here!
Your memory usage beats 46.96 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        
        def helper(node, k):
            if not node:
                return False
            if node.val in seen:
                return True
            seen.add(k - node.val)
            
            return helper(node.left, k) or helper(node.right, k)
    
        return helper(root, k)


'''
You are here!
Your runtime beats 82.55 % of python3 submissions.
You are here!
Your memory usage beats 87.72 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        q = deque([root])
        while q:
            node = q.popleft()
            if k - node.val in seen:
                return True
            seen.add(node.val)
            for child in [node.left, node.right]:
                if child:
                    q.append(child)
        return False








