'''
BFS
Topological Sort
in_degree + out_degree(graph) + deque

执行用时：40 ms, 在所有 Python3 提交中击败了66.36% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了46.68% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        out_degree = defaultdict(set)
        # b -> a
        for a, b in prerequisites:
            in_degree[a] += 1
            out_degree[b].add(a)
        
        taken = deque([i for i in range(numCourses) if i not in in_degree])
        taken_cnt = 0
        while taken:
            node = taken.popleft()
            taken_cnt += 1
            for child in out_degree[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    taken.append(child)
        return taken_cnt == numCourses

