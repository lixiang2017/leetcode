'''
DFS

执行用时：68 ms, 在所有 Python3 提交中击败了59.47% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了16.84% 的用户
通过测试用例：111 / 111
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        ans = []

        def dfs(node, parent, is_root):
            if not node:
                return
            
            if node.val in to_delete_set:
                # cut
                left, right = node.left, node.right
                node.left = None
                node.right = None 
                if parent:
                    if parent.left is node:
                        parent.left = None 
                    elif parent.right is node:
                        parent.right = None 
                dfs(left, node, True)
                dfs(right, node, True)
            else:
                dfs(node.left, node, False)
                dfs(node.right, node, False)
                if is_root:
                    ans.append(node)

        dfs(root, None, True)
        return ans 
