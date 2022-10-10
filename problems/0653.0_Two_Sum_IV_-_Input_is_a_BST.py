'''
DFS + hash table

Runtime: 425 ms, faster than 5.04% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 18 MB, less than 69.58% of Python3 online submissions for Two Sum IV - Input is a BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        seen = set()
        for x in inorder(root):
            if k - x in seen:
                return True 
            seen.add(x)
        return False


'''
DFS + two pointers

Runtime: 1329 ms, faster than 5.04% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 19.9 MB, less than 28.26% of Python3 online submissions for Two Sum IV - Input is a BST.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        
        arr = list(inorder(root))
        i, j = 0, len(arr) - 1
        while i < j:
            s = arr[i] + arr[j]
            if s == k:
                return True 
            elif s > k:
                j -= 1
            else:
                i += 1
        return False


'''
有贡献的仅为“()”，外层包裹仅起到翻倍的作用

执行用时：32 ms, 在所有 Python3 提交中击败了86.10% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了96.14% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = depth = 0
        for i, c in enumerate(s):
            depth += 1 if c == '(' else -1
            if c == ')' and s[i - 1] == '(':
                ans += 1 << depth
        return ans 
