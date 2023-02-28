'''
Runtime: 56 ms, faster than 60.60% of Python3 online submissions for Find Duplicate Subtrees.
Memory Usage: 24.4 MB, less than 27.68% of Python3 online submissions for Find Duplicate Subtrees.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ''
            serial = ''.join([str(node.val), '(', dfs(node.left), ')(', dfs(node.right), ')'])
            if (tree := seen.get(serial, None)):
                repeat.add(tree)
            else:
                seen[serial] = node
            return serial
        
        seen = dict()
        repeat = set()
        dfs(root)
        return list(repeat)
        
        