'''
DFS

执行用时：388 ms, 在所有 Python3 提交中击败了85.00% 的用户
内存消耗：44.7 MB, 在所有 Python3 提交中击败了27.50% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        @cache
        def dfs(time, mouse, cat):
            if time == 2 * n:
                return 0
            if mouse == 0:
                return 1
            if mouse == cat:
                return 2
            # mouse's turn
            if not time % 2:
                ans = 2
                for nx_node in graph[mouse]:
                    ret = dfs(time + 1, nx_node, cat)
                    if ret == 1:
                        return 1 
                    elif ret == 0:
                        ans = 0
                return ans 
            # cat's turn
            else:
                ans = 1
                for nx_node in graph[cat]:
                    if nx_node == 0:
                        continue
                    ret = dfs(time + 1, mouse, nx_node)
                    if ret == 2:
                        return 2
                    elif ret == 0:
                        ans = 0
                return ans 

        return dfs(0, 1, 2)

