'''
46 / 49 个通过测试用例
状态：超出时间限制
提交时间：几秒前
'''
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        shortest = float('inf')

        def dfs(curr_node: int, curr_len: int, curr_visited_node: Set[int],
                visited_path) -> None:
            # print('visited_path: ', visited_path)
            nonlocal shortest
            if curr_len >= shortest:
                return 
            if curr_len > max(N - 1, (N - 2) * 2):
                return 
            # print('curr_visited_node: ', curr_visited_node)
            if len(curr_visited_node) == N:
                shortest = min(shortest, curr_len)
                return

            for next_node in graph[curr_node]:
                seen = False
                # visited_path
                path = (curr_node, next_node)
                if path not in visited_path:
                    visited_path.add(path)

                    if next_node in curr_visited_node:
                        seen = True
                    else:
                        seen = False
                        curr_visited_node.add(next_node)                    
                    
                    dfs(next_node, curr_len + 1, curr_visited_node, visited_path)
                    visited_path.remove(path)
                    if not seen:
                        curr_visited_node.remove(next_node)

        #for i in range(N):
        #    dfs(i, 0, set([i]), set())
        # sorted_idx = sorted([i for i in range(N)], key=lambda i: len(graph[i]), reverse=True)  # TLE
        sorted_idx = sorted([i for i in range(N)], key=lambda i: len(graph[i]))
        for idx in sorted_idx:
            dfs(idx, 0, set([idx]), set())
        return shortest

'''
[[1,2,3],[0],[0],[0]]
[[1],[0,2,4],[1,3,4],[2],[1,2]]
[[1],[0,2,6],[1,3],[2],[5],[4,6],[1,5,7],[6]]
[[1],[0,2,6],[1,5,6],[6],[6],[2],[4,3,1,2]]
[[2,10],[2,7],[0,1,3,4,5,8],[2],[2],[2],[8],[9,11,8,1],[7,6,2],[7],[11,0],[7,10]]
[[1,2,3,4,5,6,7,8,9,10,11],[0,2,5,6,8],[0,1,4,5,6,9,10,11],[0,4,5,6,8,9,10,11],[0,2,3,5,6,8,10],[0,1,2,3,4,6,8,9,10,11],[0,1,2,3,4,5,8,10,11],[0,8],[0,1,3,4,5,6,7,9,10,11],[0,2,3,5,8,10],[0,2,3,4,5,6,8,9],[0,2,3,5,6,8]]
'''


