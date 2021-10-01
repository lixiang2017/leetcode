'''
BFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 64.89 % of python3 submissions.
You are here!
Your memory usage beats 87.34 % of python3 submissions.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good = 1
        # (node, max_value_from_root_to_current)
        q = deque([(root, root.val)])
        while q:
            node, maxn = q.popleft()
            for child in [node.left, node.right]:
                if child:
                    if child.val >= maxn:
                        q.append((child, child.val))
                        good += 1
                    else:
                        q.append((child, maxn))
        return good


'''
DFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 96.53 % of python3 submissions.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node: TreeNode, maxn: int, good: int) -> int:
            if not node:
                return good
            if node.val >= maxn:
                maxn = node.val
                good += 1
            good += dfs(node.left, maxn, 0)
            good += dfs(node.right, maxn, 0)
            return good         
            
        return dfs(root, float('-inf'), 0)


'''
没必要往里面传一个good参数
DFS
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 84.41 % of python3 submissions.
You are here!
Your memory usage beats 70.27 % of python3 submissions.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         selfIntersystem.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node: TreeNode, maxn: int) -> int:
            if not node:
                return 0
            good = 0
            if node.val >= maxn:
                maxn = node.val
                good += 1
            good += dfs(node.left, maxn)
            good += dfs(node.right, maxn)
            return good         
            
        return dfs(root, float('-inf'))

