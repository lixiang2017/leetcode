'''
802.找到最终安全状态，DFS+三色标记法+拓扑排序

执行用时：608 ms, 在所有 Python3 提交中击败了5.18% 的用户
内存消耗：87.1 MB, 在所有 Python3 提交中击败了5.12% 的用户
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0, not visited
        # 1, in stack
        # 2, safe
        state = [0] * numCourses
        # graph
        g = [[0] * numCourses for _ in range(numCourses)]
        # ingress degree
        in_deg = [0] * numCourses
        # init graph
        for post, pre in prerequisites:
            g[pre][post] = 1
            in_deg[post] += 1

        def safe(i):
            if state[i]:
                return state[i] == 2
            state[i] = 1
            for y, value in enumerate(g[i]):
                if value and not safe(y):
                    return False
            state[i] = 2
            return True
        # check 
        for i in range(numCourses):
            if not safe(i):
                return []
        
        q = deque([i for i in range(numCourses) if 0 == in_deg[i]])
        ans = list(q)
        while q:
            node = q.popleft()
            for i in range(numCourses):
                if g[node][i]:
                    in_deg[i] -= 1
                    if 0 == in_deg[i]:
                        q.append(i)
                        ans.append(i)
        return ans
