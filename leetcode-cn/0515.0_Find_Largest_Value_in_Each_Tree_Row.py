'''
BFS
T: O(N)
S: O(N)

执行用时：48 ms, 在所有 Python3 提交中击败了81.49% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了40.90% 的用户
通过测试用例：78 / 78
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans, q = [], [root] if root else []
        while q:
            next_q = []
            ans.append(q[0].val)
            for node in q:
                ans[-1] = max(ans[-1], node.val)
                for child in [node.left, node.right]:
                    if child:
                        next_q.append(child)
            q = next_q
        return ans 


'''
DFS

执行用时：48 ms, 在所有 Python3 提交中击败了81.49% 的用户
内存消耗：18.2 MB, 在所有 Python3 提交中击败了5.18% 的用户
通过测试用例：78 / 78
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return 
            if len(ans) < depth:
                ans.append(node.val)
            else:
                ans[depth - 1] = max(ans[depth - 1], node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return ans 


