'''
recursion
T: O(2*N + NlogN)
S: O(2*N)

Runtime: 116 ms, faster than 32.79% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 14.4 MB, less than 5.31% of Python3 online submissions for Recover Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
                
        nums = sorted(list(inorder(root)))
        i = 0
        def recover(node):
            nonlocal nums, i
            if not node:
                return 
            recover(node.left)
            node.val = nums[i]
            i += 1
            recover(node.right)
            
        recover(root)

        
'''
recursion
step:
1、寻找异常值，prev_val > cur_val，prev node 即为first
2、寻找异常值，prev_val > cur_val，cur node 即为second
或者在找到first后，寻找右侧的最小值
3、swap values

Runtime: 98 ms, faster than 52.35% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 14.3 MB, less than 28.16% of Python3 online submissions for Recover Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = second = None
        def inorder(node):
            nonlocal prev, first, second
            if not node:
                return 
            inorder(node.left)
            if first is None and prev and prev.val > node.val:
                first = prev
            if first is not None and prev and prev.val > node.val:
                second = node
            prev = node 
            inorder(node.right)
            
        inorder(root)
        # swap
        first.val, second.val = second.val, first.val 
        
'''
recursion
或者在找到first后，寻找右侧的最小值

Runtime: 108 ms, faster than 40.96% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 14.2 MB, less than 94.87% of Python3 online submissions for Recover Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = second = None
        def inorder(node):
            nonlocal prev, first, second
            if not node:
                return 
            inorder(node.left)
            if first is None and prev and prev.val > node.val:
                first = prev
            if first is not None and (not second or second.val > node.val):
                second = node
            prev = node 
            inorder(node.right)
            
        inorder(root)
        # swap
        first.val, second.val = second.val, first.val 
        
'''
iteration
T: O(N)
S: O(H), H is height of the tree for stack.

Runtime: 79 ms, faster than 79.52% of Python3 online submissions for Recover Binary Search Tree.
Memory Usage: 14.2 MB, less than 65.76% of Python3 online submissions for Recover Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = second = None
        node, stack = root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if first is None and prev and prev.val > node.val:
                    first = prev
                if first is not None and (not second or second.val > node.val):
                    second = node
                prev = node 
                # move to right
                node = node.right
            
        # swap
        first.val, second.val = second.val, first.val 
        



