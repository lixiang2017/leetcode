'''
DFS

执行用时：40 ms, 在所有 Python3 提交中击败了15.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了12.89% 的用户
通过测试用例：208 / 208
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []

        def dfs(node: TreeNode, path: str):
            if not node:
                return 
            if not node.left and not node.right:
                ans.append(path)
                return 
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))

        dfs(root, str(root.val))
        return ans

'''
DFS

执行用时：32 ms, 在所有 Python3 提交中击败了75.99% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.18% 的用户
通过测试用例：208 / 208
'''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []

        def dfs(node: TreeNode, path: str):
            if not node.left and not node.right:
                ans.append(path)
                return 
            if node.left:
                dfs(node.left, path + '->' + str(node.left.val))
            if node.right:
                dfs(node.right, path + '->' + str(node.right.val))

        dfs(root, str(root.val))
        return ans




'''
BFS

执行用时：36 ms, 在所有 Python3 提交中击败了47.73% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了88.51% 的用户
通过测试用例：208 / 208
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        ans = []
        # (node, path)
        q = deque([(root, str(root.val))])
        while q:
            node, path = q.popleft()
            if not node.left and not node.right:
                ans.append(path)
            for child in [node.left, node.right]:
                if child:
                    q.append((child, path + '->' + str(child.val)))

        return ans
