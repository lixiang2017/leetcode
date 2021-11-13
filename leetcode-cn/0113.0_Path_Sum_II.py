'''
BFS

执行用时：40 ms, 在所有 Python3 提交中击败了83.54% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了95.45% 的用户
通过测试用例：115 / 115
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        q = deque()
        if root:
            # [node, cur_sum, root-to-cur-list]
            q.append([root, root.val, [root.val]])
        while q:
            node, cur_sum, cur_path = q.popleft()
            if node.left:
                q.append([node.left, cur_sum + node.left.val, cur_path + [node.left.val] ])
            if node.right:
                q.append([node.right, cur_sum + node.right.val, cur_path + [node.right.val]])
            if not node.left and not node.right and cur_sum == targetSum:
                ans.append(cur_path)

        return ans

'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了83.54% 的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了22.32% 的用户
通过测试用例：115 / 115
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return []
        
        def dfs(node: Optional[TreeNode], cur_sum: int, cur_path: List[int]):
            if node.left:
                dfs(node.left, cur_sum + node.left.val, cur_path + [node.left.val])
            if node.right:
                dfs(node.right, cur_sum + node.right.val, cur_path + [node.right.val])
            if not node.left and not node.right and cur_sum == targetSum:
                ans.append(cur_path)
        
        dfs(root, root.val, [root.val])
        return ans

