'''
DFS

Runtime: 20 ms, faster than 98.97% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.3 MB, less than 47.19% of Python3 online submissions for Binary Tree Inorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return list(chain(self.inorderTraversal(root.left), [root.val], self.inorderTraversal(root.right))) if root else []

'''
DFS

Runtime: 35 ms, faster than 9.57% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.4 MB, less than 14.05% of Python3 online submissions for Binary Tree Inorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


'''
Iteration

Runtime: 32 ms, faster than 56.91% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.2 MB, less than 47.19% of Python3 online submissions for Binary Tree Inorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        
        return ans



'''
Morris
T: O(2N)
S: O(1)
ref:
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/
https://leetcode.com/problems/binary-tree-inorder-traversal/solution/

Runtime: 28 ms, faster than 82.40% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 14.2 MB, less than 76.21% of Python3 online submissions for Binary Tree Inorder Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr = root
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right, curr.left, curr = curr, None, curr.left
            else:
                ans.append(curr.val)
                curr = curr.right
        
        return ans
        


