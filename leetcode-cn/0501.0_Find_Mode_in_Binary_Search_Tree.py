'''
recursion for inorder
T: O(N)
S: O(1)

执行用时：56 ms, 在所有 Python3 提交中击败了70.08% 的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了42.18% 的用户
通过测试用例：23 / 23
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        max_freq = freq = 0
        x = -200000

        def inorder(node):
            nonlocal ans, max_freq, freq, x
            if not node:
                return 
            inorder(node.left)
            if node.val != x:
                x = node.val
                freq = 1
            else:
                freq += 1
            if freq > max_freq:
                max_freq = freq 
                ans = [x]
            elif freq == max_freq:
                ans.append(x)
            inorder(node.right)

        inorder(root)
        return ans 

'''
iteration for inorder

执行用时：56 ms, 在所有 Python3 提交中击败了70.23% 的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了68.15% 的用户
通过测试用例：23 / 23
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        max_freq = freq = 0
        x = -200000
        node, stack = root, []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left 
            else:
                node = stack.pop()
                # do the real thing
                if node.val != x:
                    x = node.val
                    freq = 1
                else:
                    freq += 1
                if freq > max_freq:
                    max_freq = freq 
                    ans = [x]
                elif freq == max_freq:
                    ans.append(x)
                # move to right
                node = node.right 
        return ans 


