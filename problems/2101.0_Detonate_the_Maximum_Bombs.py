'''
Runtime: 519 ms, faster than 89.95% of Python3 online submissions for Detonate the Maximum Bombs.
Memory Usage: 16.7 MB, less than 39.23% of Python3 online submissions for Detonate the Maximum Bombs.
'''
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = defaultdict(list)
        # from i to j
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                dx, dy = x1 - x2, y1 - y2
                dd = dx * dx + dy * dy
                if dd <= r1 * r1:
                    g[i].append(j)
        ans = 1
        for i in range(n):
            # start from i 
            seen = {i}
            q = deque([i])
            while q:
                node = q.popleft()
                for child in g[node]:
                    if child not in seen:
                        seen.add(child)
                        q.append(child)
            ans = max(ans, len(seen))
        return ans 


'''
Runtime: 247 ms, faster than 95.56% of Python3 online submissions for Detonate the Maximum Bombs.
Memory Usage: 16.5 MB, less than 55.17% of Python3 online submissions for Detonate the Maximum Bombs.
'''
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = defaultdict(list)
        # from i to j
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                dx, dy = x1 - x2, y1 - y2
                dd = dx * dx + dy * dy
                if dd <= r1 * r1:
                    g[i].append(j)
        ans = 1
        for i in range(n):
            # start from i 
            seen = {i}
            q = deque([i])
            while q:
                node = q.popleft()
                for child in g[node]:
                    if child not in seen:
                        seen.add(child)
                        q.append(child)
            ans = max(ans, len(seen))
            if ans == n:
                return n
        return ans 


'''
Runtime: 241 ms, faster than 95.75% of Python3 online submissions for Detonate the Maximum Bombs.
Memory Usage: 16.6 MB, less than 48.31% of Python3 online submissions for Detonate the Maximum Bombs.
'''
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = defaultdict(list)
        # from i to j
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                dx, dy = x1 - x2, y1 - y2
                dd = dx * dx + dy * dy
                if dd <= r1 * r1:
                    g[i].append(j)
        ans = 1
        indice = list(range(n))
        indice.sort(key = lambda i: -len(g[i]))
        for i in indice:
            # start from i 
            seen = {i}
            q = deque([i])
            while q:
                node = q.popleft()
                for child in g[node]:
                    if child not in seen:
                        seen.add(child)
                        q.append(child)
            if len(seen) > ans:
                ans = len(seen)
                if ans == n:
                    return n
        return ans 


        