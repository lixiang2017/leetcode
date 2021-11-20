'''
DFS, post order

执行用时：56 ms, 在所有 Python3 提交中击败了54.26% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了92.46% 的用户
通过测试用例：77 / 77
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        t = 0

        def dfs(node: TreeNode):
            nonlocal t
            if not node:
                return 0
            sum_left = dfs(node.left)
            sum_right = dfs(node.right)
            t += abs(sum_left - sum_right)
            return sum_left + sum_right + node.val
        
        dfs(root)
        return t


'''
DFS, self

执行用时：48 ms, 在所有 Python3 提交中击败了88.73% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了92.33% 的用户
通过测试用例：77 / 77
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node: TreeNode):
        if not node:
            return 0
        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_left - sum_right)
        return sum_left + sum_right + node.val


'''
BFS, post orde

执行用时：56 ms, 在所有 Python3 提交中击败了53.96% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了99.52% 的用户
通过测试用例：77 / 77
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        stk = [root]
        tree = deque()
        while stk:
            node = stk.pop()
            tree.appendleft(node)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)

        ans = 0
        for node in tree:
            left = right = 0
            if node.left:
                left = node.left.val
            if node.right:
                right = node.right.val
            ans += abs(left - right)
            node.val += left + right
        return ans


