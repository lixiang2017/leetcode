'''
DFS

执行用时：108 ms, 在所有 Python3 提交中击败了8.61% 的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了7.52% 的用户
通过测试用例：35 / 35
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        def dfs(node: TreeNode, val: int):
            if not node:
                return
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    dfs(node.right, val)
            elif node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return 
                else:
                    dfs(node.left, val)
    
        dfs(root, val)
        return root


'''
BFS

执行用时：92 ms, 在所有 Python3 提交中击败了38.56% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了76.36% 的用户
通过测试用例：35 / 35
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                else:
                    q.append(node.right)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    q.append(node.left)

        return root

'''
BFS

执行用时：84 ms, 在所有 Python3 提交中击败了83.77% 的用户
内存消耗：17.2 MB, 在所有 Python3 提交中击败了5.01% 的用户
通过测试用例：35 / 35
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        pos = root
        while pos:
            if pos.val < val:
                if not pos.right:
                    pos.right = TreeNode(val)
                    break
                else:
                    pos = pos.right
            else:
                if not pos.left:
                    pos.left = TreeNode(val)
                    break
                else:
                    pos = pos.left

        return root


