'''
inorder + two pointers

执行用时：880 ms, 在所有 Python3 提交中击败了5.07% 的用户
内存消耗：20.7 MB, 在所有 Python3 提交中击败了40.50% 的用户
通过测试用例：422 / 422
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node: Optional[TreeNode]):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        nums = list(inorder(root))
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s == k:
                return True
            elif s < k:
                i += 1
            else:
                j -= 1
        return False

