'''
BFS
T: O(N)
S: O(logN)

Runtime: 90 ms, faster than 13.14% of Python3 online submissions for Maximum Width of Binary Tree.
Memory Usage: 14.8 MB, less than 69.75% of Python3 online submissions for Maximum Width of Binary Tree.
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
        q = deque([(root, 0)])
        while q:
            while q and q[-1][0] == None:
                q.pop()
            while q and q[0][0] == None:
                q.popleft()
            if not q:
                break

            ans = max(ans, q[-1][1] - q[0][1] + 1)
            next_q = deque()
            for node, x in q:
                if node:
                    next_q.append((node.left, 2 * x + 1))
                    next_q.append((node.right, 2 * x + 2))
            q = next_q
        
        return ans
        
