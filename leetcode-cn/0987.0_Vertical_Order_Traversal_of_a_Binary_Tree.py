'''
Hash Table + DFS + Sort

执行用时：36 ms, 在所有 Python3 提交中击败了86.88% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了10.29% 的用户
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # column -> [(row, node_value)]
        c2nodes = defaultdict(list)

        def dfs(node: TreeNode, r: int, c: int):
            '''node, row, column'''
            if not node:
                return
            
            c2nodes[c].append((r, node.val))
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)
        
        dfs(root, 0, 0)
        # c_nodes = sorted([c, nodes] for c, nodes in c2nodes.items())  # wrong for nodes
        c_nodes = sorted([c, sorted(nodes)] for c, nodes in c2nodes.items())
        return [[val for _, val in nodes] for c, nodes in c_nodes]
        '''
        ans = []
        for c, nodes in c_nodes:
            vertical = []
            for row, node_value in nodes:
                vertical.append(node_value)
            ans.append(vertical)

        return ans
        '''
