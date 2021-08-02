'''
Hash Table + DFS,T:O(2N),S:O(2N)

执行用时：32 ms, 在所有 Python3 提交中击败了98.88% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了87.68% 的用户
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parents = {root: None}  # to avoid key error

        def findParents(node: TreeNode):
            if not node:
                return
            for child in [node.left, node.right]:
                if child:
                    parents[child] = node
                    findParents(child)

        def findAns(node: TreeNode, from_node: TreeNode, dept: int, k: int):
            if not node:
                return
            if dept == k:
                ans.append(node.val)
                return

            for next_node in [parents[node], node.left, node.right]:
                if next_node != from_node:
                    findAns(next_node, node, dept + 1, k)

        findParents(root)
        findAns(target, None, 0, k)
        return ans



'''
Hash Table(build graph) + BFS,T:O(2N),S:O(2N)

执行用时：40 ms, 在所有 Python3 提交中击败了86.55% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了38.38% 的用户
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
        def build_graph(node: TreeNode, parent: TreeNode):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            build_graph(node.left, node)
            build_graph(node.right, node)

        ans = []
        q = deque([target.val])
        visited = set([target.val])
        build_graph(root, None)
        while q:
            if 0 == k:
                return list(q)
                
            for _ in range(len(q)):
                val = q.popleft()
                for child in graph[val]:
                    if child not in visited:
                        visited.add(child)
                        q.append(child)

            k -= 1
        return ans
