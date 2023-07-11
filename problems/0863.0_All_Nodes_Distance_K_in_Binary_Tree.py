'''
Runtime: 50 ms, faster than 79.58% of Python3 online submissions for All Nodes Distance K in Binary Tree.
Memory Usage: 16.8 MB, less than 35.25% of Python3 online submissions for All Nodes Distance K in Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)
        build_graph(root, None)
    
        ans = []
        visited = set([target.val])
        
        def dfs(cur, distance):
            if distance == k:
                ans.append(cur)
                return 
            for neighbor in graph[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, distance + 1)
                    
        dfs(target.val, 0)
        return ans
        