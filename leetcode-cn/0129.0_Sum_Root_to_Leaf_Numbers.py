'''
BFS
T: O(N)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了65.27% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了58.43% 的用户
通过测试用例：108 / 108
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([(root, root.val)])
        while q:
            node, s = q.popleft()
            if not node.left and not node.right:
                ans += s 
            if node.left:
                q.append((node.left, s * 10 + node.left.val))
            if node.right:
                q.append((node.right, s * 10 + node.right.val))

        return ans 

