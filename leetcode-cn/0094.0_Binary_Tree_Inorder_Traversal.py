'''
approach: One Line / DFS

执行用时：44 ms, 在所有 Python3 提交中击败了32.70%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了98.79%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return list(chain(self.inorderTraversal(root.left), [root.val], self.inorderTraversal(root.right))) if root else []


'''
iteration stack
T: O(N)
S: O(H)

执行用时：32 ms, 在所有 Python3 提交中击败了87.58% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.57% 的用户
通过测试用例：70 / 70
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node, ans, stack = root, [], []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left 
            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right 

        return ans 
