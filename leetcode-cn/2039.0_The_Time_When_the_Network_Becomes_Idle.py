'''
BFS


执行用时：724 ms, 在所有 Python3 提交中击败了20.45% 的用户
内存消耗：76.6 MB, 在所有 Python3 提交中击败了9.09% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        # graph
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        dist = [0] * n
        seen = set([0])
        # (node, step)
        q = deque([(0, 0)])
        while q:
            node, step = q.popleft()
            for child in g[node]:
                if child not in seen:
                    dist[child] = step + 1 
                    q.append((child, step + 1))
                    seen.add(child)

        ans = 0
        for i in range(1, n):
            p = patience[i]
            circle = dist[i] * 2
            if circle <= p:
                ans = max(ans, circle)
            else:
                # suppose dist[i]=8, circle=16, p=5
                # 0 .....  16
                #        15 ...... 15+circle
                _, r = divmod(circle, p)
                if r != 0:
                    ans = max(ans, 2 * circle - r)
                else:
                    # suppose dist[i]=8, circle=16, p=4
                    # 0 .....  16
                    #       12 ...... 12+circle      
                    ans = max(ans, 2 * circle - p)

        return ans + 1


'''
BFS
ans = max(ans, (circle - 1) // p * p + circle)
这个计算时间的方法厉害了。有时候，cost - 1 再取余，是个非常常见的技巧。 -1 ！！！

执行用时：700 ms, 在所有 Python3 提交中击败了25.00% 的用户
内存消耗：76.2 MB, 在所有 Python3 提交中击败了11.36% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        # graph
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        dist = [0] * n
        seen = set([0])
        # (node, step)
        q = deque([(0, 0)])
        while q:
            node, step = q.popleft()
            for child in g[node]:
                if child not in seen:
                    dist[child] = step + 1 
                    q.append((child, step + 1))
                    seen.add(child)

        ans = 0
        for i in range(1, n):
            p = patience[i]
            circle = dist[i] * 2
            ans = max(ans, (circle - 1) // p * p + circle)
        return ans + 1


'''
BFS, calculate answer in while, no need distance array

执行用时：696 ms, 在所有 Python3 提交中击败了25.00% 的用户
内存消耗：77.3 MB, 在所有 Python3 提交中击败了6.82% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        # graph
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        
        ans, seen = 0, set([0])
        # (node, step)
        q = deque([(0, 0)])
        while q:
            node, step = q.popleft()
            for child in g[node]:
                if child not in seen:
                    q.append((child, step + 1))
                    seen.add(child)
                    # calculate answer in while, no need distance array
                    p = patience[child]
                    circle = (step + 1) * 2
                    ans = max(ans, (circle - 1) // p * p + circle)
            
        return ans + 1











