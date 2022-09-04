'''
DFS + hash table

Runtime: 36 ms, faster than 92.24% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
Memory Usage: 14.2 MB, less than 72.74% of Python3 online submissions for Vertical Order Traversal of a Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical = defaultdict(dict) 
        leftmost = rightmost = 0
        
        def dfs(node, row, col):
            nonlocal leftmost, rightmost
            if row in vertical[col]:
                vertical[col][row].append(node.val)
            else:
                vertical[col][row] = [node.val]
            if node.left:
                dfs(node.left, row + 1, col - 1)
                leftmost = min(leftmost, col - 1)
            if node.right:
                dfs(node.right, row + 1, col + 1)
                rightmost = max(rightmost, col + 1)
                
        if root:
            dfs(root, 0, 0)
        
        ans = []
        for j in range(leftmost, rightmost + 1):
            # values for every vertical line
            values = []
            row_indice = sorted(vertical[j].keys())
            for i in row_indice:
                values.extend(sorted(vertical[j][i]))
            ans.append(values)
        return ans 
    
'''
Wrong Answer
Details
Input
[3,1,4,0,2,2]
Output
[[0],[1],[2,2,3],[4]]
Expected
[[0],[1],[3,2,2],[4]]
'''

