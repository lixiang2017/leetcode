'''
BFS
T: O(N)
S: O(width of the binary tree) = O(N)

执行用时：60 ms, 在所有 Python3 提交中击败了12.80% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了46.97% 的用户
通过测试用例：114 / 114
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = [(root, 0)] if root else []
        while q:
            ans = max(q[-1][1] - q[0][1] + 1, ans)
            next_q = []
            for node, idx in q:
                if node.left:
                    next_q.append([node.left, idx * 2])
                if node.right:
                    next_q.append([node.right, idx * 2 + 1])
            q = next_q
        return ans 
