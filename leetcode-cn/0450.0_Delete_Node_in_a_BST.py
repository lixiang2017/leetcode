'''
DFS, 分情况讨论，寻找右子树的最左节点
递归删除每一次的最小值 deleteNode(root.right, min_node.val)
这种写法不会造成 BST 的高度增长

执行用时：48 ms, 在所有 Python3 提交中击败了99.18% 的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了65.24% 的用户
通过测试用例：91 / 91
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None 
            if not root.left:
                return root.right
            if not root.right:
                return root.left 
            min_node = root.right 
            while min_node.left:
                min_node = min_node.left 
            root.val = min_node.val 
            root.right = self.deleteNode(root.right, min_node.val)

        return root 
