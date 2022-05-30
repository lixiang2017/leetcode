'''
DFS

执行用时：36 ms, 在所有 Python3 提交中击败了96.13% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了84.52% 的用户
通过测试用例：63 / 63
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, cur):
            nonlocal ans 
            if not node:
                return 
            cur *= 2
            cur += node.val 
            if not node.left and not node.right:
                ans += cur 
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, 0)
        return ans 

'''
BFS

执行用时：52 ms, 在所有 Python3 提交中击败了19.03% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了21.94% 的用户
通过测试用例：63 / 63
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = [(root, 0)]
        while q:
            next_q = []
            for node, cur in q:
                cur *= 2
                cur += node.val                
                if not node.left and not node.right:
                    ans += cur 
                    continue
                if node.left:
                    next_q.append((node.left, cur))
                if node.right:
                    next_q.append((node.right, cur))
            q = next_q
        return ans 



