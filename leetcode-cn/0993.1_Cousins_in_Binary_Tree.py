'''
approach: DFS
Time: O(N)
Space: O(N)

执行用时：60 ms, 在所有 Python3 提交中击败了7.75% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了53.68% 的用户
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent, x_depth, x_found = None, None, False
        y_parent, y_depth, y_found = None, None, False

        def dfs(node: TreeNode, depth: int, parent: TreeNode):
            if not node:
                return 
            
            nonlocal x_parent, x_depth, x_found, y_parent, y_depth, y_found
        
            if node.val == x:
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                y_parent, y_depth, y_found = parent, depth, True
            
            if x_found and y_found:
                return
            
            dfs(node.left, depth + 1, node)
            if x_found and y_found:
                return 
            dfs(node.right, depth + 1, node)
        
        dfs(root, 0, None)

        return x_depth == y_depth and x_parent != y_parent



'''
approach: BFS
Time: O(N)
Space: O(N)

执行用时：44 ms, 在所有 Python3 提交中击败了53.28% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了39.36% 的用户
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent, x_depth, x_found = None, None, False
        y_parent, y_depth, y_found = None, None, False

        def update(node: TreeNode, depth: int, parent: TreeNode):
            if node.val == x:
                nonlocal x_parent, x_depth, x_found
                x_parent, x_depth, x_found = parent, depth, True
            elif node.val == y:
                nonlocal y_parent, y_depth, y_found
                y_parent, y_depth, y_found = parent, depth, True
        
        q = collections.deque([(root, 0)])
        update(root, 0, None)

        while q:
            node, depth = q.popleft()
            if node.left:
                q.append((node.left, depth + 1))
                update(node.left, depth + 1, node)
            if node.right:
                q.append((node.right, depth + 1))
                update(node.right, depth + 1, node)

            if x_found and y_found:
                break

        return x_depth == y_depth and x_parent != y_parent
