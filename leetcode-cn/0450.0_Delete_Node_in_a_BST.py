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


'''
DFS, 分类讨论，
找到要删除节点，把左子树接在[右子树的最左节点的left孩子]
这个写法会导致树增高

执行用时：64 ms, 在所有 Python3 提交中击败了52.17% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了11.43% 的用户
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
            min_node.left = root.left
            return root.right

        return root


'''
DFS, 分类讨论，
找到要删除节点，把右子树接在[左子树的最右节点的right孩子]
这个写法会导致树增高

执行用时：64 ms, 在所有 Python3 提交中击败了52.17% 的用户
内存消耗：19.5 MB, 在所有 Python3 提交中击败了49.81% 的用户
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
            # find right_most node in left_child
            max_node = root.left 
            while max_node.right:
                max_node = max_node.right 
            max_node.right = root.right 
            return root.left 

        return root



'''
reconstruct BST

执行用时：96 ms, 在所有 Python3 提交中击败了6.25% 的用户
内存消耗：21.2 MB, 在所有 Python3 提交中击败了5.02% 的用户
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
        def inorder(node: Optional[TreeNode]):
            if node:
                yield from inorder(node.left)
                if node.val != key:
                    yield node.val 
                yield from inorder(node.right)
        
        arr = list(inorder(root))

        def construct(l, r):
            if l > r:
                return None 
            if l == r:
                return TreeNode(arr[l])
            mid = (l + r) // 2
            return TreeNode(arr[mid], construct(l, mid - 1), construct(mid + 1, r))

        return construct(0, len(arr) - 1)











