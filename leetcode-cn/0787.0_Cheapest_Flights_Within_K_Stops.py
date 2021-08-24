'''
BFS with pruning

执行用时：32 ms, 在所有 Python3 提交中击败了99.40% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了44.35% 的用户
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # graph
        g = defaultdict(dict)
        for u, v, w in flights:
            g[u][v] = w

        distance = [float('inf')] * n
        tries = [(src, 0)]
        for _ in range(k + 1):
            level = []
            for i, cost in tries:
                for j, price in g[i].items():
                    t = cost + price
                    if t < distance[j] and t < distance[dst]:  # pruning
                        distance[j] = t
                        level.append((j, t))
            tries = level

        return distance[dst] if distance[dst] != float('inf') else -1


'''
BFS with pruning

执行用时：32 ms, 在所有 Python3 提交中击败了99.40% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了32.89% 的用户
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # graph
        g = defaultdict(list)
        for u, v, w in flights:
            g[u].append((v, w))

        distance = [float('inf')] * n
        tries = [(src, 0)]
        while k >= 0:
            level = []
            for i, cost in tries:
                for j, price in g[i]:
                    t = cost + price
                    if t < distance[j] and t < distance[dst]:  # pruning
                        distance[j] = t
                        if j != dst:
                            level.append((j, t))
            tries = level
            k -= 1

        return distance[dst] if distance[dst] != float('inf') else -1


'''
DP

执行用时：152 ms, 在所有 Python3 提交中击败了66.22% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了84.82% 的用户
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [float('inf')] * n
        ans = float('inf')
        f[src] = 0

        for _ in range(k + 1):
            g = [float('inf')] * n
            for i, j, p in flights:
                # g[j] = min(f[j], f[i] + p)  # wrong
                g[j] = min(g[j], f[i] + p)
            ans = min(ans, g[dst])
            f = g

        return ans if ans != float('inf') else -1

