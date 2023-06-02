'''
执行用时：368 ms, 在所有 Python3 提交中击败了92.73% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了28.18% 的用户
通过测试用例：160 / 160
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
执行用时：160 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了25.45% 的用户
通过测试用例：160 / 160
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
执行用时：164 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了21.82% 的用户
通过测试用例：160 / 160
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
