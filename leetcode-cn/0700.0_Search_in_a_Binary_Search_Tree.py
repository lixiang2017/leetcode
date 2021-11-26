'''
DFS

执行用时：76 ms, 在所有 Python3 提交中击败了22.81% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了30.02% 的用户
通过测试用例：36 / 36
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def dfs(node: TreeNode, val: int):
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val < val:
                return dfs(node.right, val)
            else:
                return dfs(node.left, val)
        
        return dfs(root, val)


'''
BFS

执行用时：76 ms, 在所有 Python3 提交中击败了22.81% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了12.31% 的用户
通过测试用例：36 / 36
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                return None
            if node.val == val:
                return node
            elif node.val < val:
                q.append(node.right)
            else:
                q.append(node.left)
        
        return None

'''
BFS

执行用时：68 ms, 在所有 Python3 提交中击败了64.80% 的用户
内存消耗：16.9 MB, 在所有 Python3 提交中击败了42.87% 的用户
通过测试用例：36 / 36
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            elif node.val < val:
                if node.right:
                    q.append(node.right)
            else:
                if node.left:
                    q.append(node.left)
        
        return None



