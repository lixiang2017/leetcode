'''
Topological Sort

执行用时：72 ms, 在所有 Python3 提交中击败了74.26% 的用户
内存消耗：20.5 MB, 在所有 Python3 提交中击败了51.49% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        in_degree = [0] * n
        graph = defaultdict(list)
        # [1, 0], 1 richer than 0, 1 -> 0
        for a, b in richer:
            # a -> b
            graph[a].append(b)
            in_degree[b] += 1

        quiet2person = {q_value: i for i, q_value in enumerate(quiet)}
        q = deque([i for i, d in enumerate(in_degree) if d == 0])
        while q:
            node = q.popleft()
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)
                quiet[child] = min(quiet[child], quiet[node])
        return [quiet2person[q_value] for q_value in quiet]


