'''
DFS

执行用时：48 ms, 在所有 Python3 提交中击败了41.89% 的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了17.75% 的用户
通过测试用例：31 / 31
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = convert(l, mid - 1)
            node.right = convert(mid + 1, r)
            return node 
        
        return convert(0, len(nums) - 1)
