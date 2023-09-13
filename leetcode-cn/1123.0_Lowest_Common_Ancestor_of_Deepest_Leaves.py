'''
60ms 击败 40.91%使用 Python3 的用户
16.26MB 击败 42.73%使用 Python3 的用户
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth2nodes_indice = defaultdict(list)
        index2node = dict()

        def dfs(node, index, depth):
            if not node:
                return 
            index2node[index] = node 
            depth2nodes_indice[depth].append(index)
            dfs(node.left, 2 * index, depth + 1)
            dfs(node.right, 2 * index + 1, depth + 1)

        dfs(root, 1, 0)

        max_depth = max(depth2nodes_indice)
        deepest_indice = set(depth2nodes_indice[max_depth])
        while len(deepest_indice) > 1:
            deepest_indice = set(i // 2 for i in deepest_indice)

        return index2node[deepest_indice.pop()]
