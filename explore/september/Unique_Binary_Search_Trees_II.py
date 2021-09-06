'''
DFS
 
You are here!
Your runtime beats 12.50 % of python3 submissions.
You are here!
Your memory usage beats 58.47 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            for i in range(start, end + 1):
                lefts = generateTrees(start, i - 1)
                rights = generateTrees(i + 1, end)
                for l in lefts:
                    for r in rights:
                        curr = TreeNode(i, l, r)
                        allTrees.append(curr)
            return allTrees
        
        return generateTrees(1, n) if n else []
