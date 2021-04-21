'''
approach: Iteration / Stack
Time: O(N)
Space: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了82.92%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了78.99%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        stack, output = [root], []
        while stack:
            node = stack.pop(-1)
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output



'''
approach: One Line / DFS
Time: O(N)
Space: O(N)

执行用时：56 ms, 在所有 Python3 提交中击败了5.44%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了57.25%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return list(chain([root.val], self.preorderTraversal(root.left), self.preorderTraversal(root.right))) if root else []
