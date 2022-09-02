'''
BFS
T: O(2N)
S: O(logN)

Runtime: 77 ms, faster than 56.40% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.6 MB, less than 46.07% of Python3 online submissions for Average of Levels in Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = [root] if root else []
        while q:
            total = sum(node.val for node in q) / len(q)
            ans.append(total)
            q = [child for node in q for child in [node.left, node.right] if child]
        return ans 
