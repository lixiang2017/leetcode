'''
BFS
T: O(N)
S: O(N)

执行用时：408 ms, 在所有 Python3 提交中击败了54.96% 的用户
内存消耗：43.7 MB, 在所有 Python3 提交中击败了17.56% 的用户
通过测试用例：105 / 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q, level = deque([root]), 0
        while q:
            pre_val = None
            for i in range(len(q)):
                node = q.popleft()
                if not pre_val:
                    pre_val = node.val
                    if not (pre_val & 1) ^ (level & 1):
                        return False
                else:
                    if not (node.val & 1) ^ (level & 1):
                        return False                    
                    if level % 2 == 0 and node.val <= pre_val:
                        return False
                    if level % 2 == 1 and node.val >= pre_val:
                        return False 
                    pre_val = node.val 
                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
            level += 1

        return True 

'''
DFS
T: O(N)
S: O(logN)

执行用时：428 ms, 在所有 Python3 提交中击败了48.85% 的用户
内存消耗：134.2 MB, 在所有 Python3 提交中击败了7.63% 的用户
通过测试用例：105 / 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.level2pre = dict()
        return self.dfs(root, 0)

    def dfs(self, node: Optional[TreeNode], level: int) -> bool:
        pre = self.level2pre.get(level)
        if pre is None:
            pre = 10**6 if level & 1 else 0
        cur = node.val 
        if not (level & 1) ^ (cur & 1):
            return False 
        # odd
        if (level & 1) and (pre <= cur): return False 
        # even
        if not (level & 1) and (pre >= cur): return False
        self.level2pre[level] = cur 
        if node.left and not self.dfs(node.left, level + 1):
            return False 
        if node.right and not self.dfs(node.right, level + 1):
            return False 
        return True 

