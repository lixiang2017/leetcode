'''
BFS

执行用时：1196 ms, 在所有 Python3 提交中击败了18.46% 的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了36.92% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked_set = set(tuple(b) for b in blocked)

        def bfs(start: List[int], end: List[int]):
            # source -> target, or target -> source
            seen = set(tuple(start))
            q = deque([start])
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < 1000_000 and 0 <= ny < 1000_000 and (nx, ny) not in blocked_set and \
                            (nx, ny) not in seen:
                        if end == [nx, ny]:
                            return 'Found'
                        seen.add((nx, ny))
                        q.append([nx, ny])

                if len(seen) > 200 * 200 // 2:
                    return 'UnBounded'
            return 'Bounded'
        
        t1 = bfs(source, target)
        t2 = bfs(target, source)
        if t1 == 'Found' or t2 == 'Found':
            return True
        if t1 == 'Bounded' or t2 == 'Bounded':
            return False 
        return True 
                    
'''
BFS

执行用时：1040 ms, 在所有 Python3 提交中击败了23.08% 的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了32.31% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked_set = set(tuple(b) for b in blocked)

        def bfs(start: List[int], end: List[int]):
            # source -> target, or target -> source
            seen = set(tuple(start))
            q = deque([start])
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < 1000_000 and 0 <= ny < 1000_000 and (nx, ny) not in blocked_set and \
                            (nx, ny) not in seen:
                        if end == [nx, ny]:
                            return 'Found'
                        seen.add((nx, ny))
                        q.append([nx, ny])

                if len(seen) > 200 * 200 // 2:
                    return 'UnBounded'
            return 'Bounded'
        
        t1 = bfs(source, target)
        if t1 == 'Found':
            return True  
        if t1 == 'Bounded':
            return False       
        t2 = bfs(target, source)
        if t2 == 'Found':
            return True
        if t2 == 'Bounded':
            return False 
        return True 



'''
BFS
200 * 199 // 2

执行用时：936 ms, 在所有 Python3 提交中击败了29.23% 的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了32.31% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked_set = set(tuple(b) for b in blocked)

        def bfs(start: List[int], end: List[int]):
            # source -> target, or target -> source
            seen = set([tuple(start)])
            q = deque([start])
            while q:
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < 1000_000 and 0 <= ny < 1000_000 and (nx, ny) not in blocked_set and \
                            (nx, ny) not in seen:
                        if end == [nx, ny]:
                            return 'Found'
                        seen.add((nx, ny))
                        q.append([nx, ny])

                if len(seen) > 200 * 199 // 2:
                    return 'UnBounded'
            return 'Bounded'
        
        t1 = bfs(source, target)
        if t1 == 'Found':
            return True  
        if t1 == 'Bounded':
            return False       
        t2 = bfs(target, source)
        if t2 == 'Found':
            return True
        if t2 == 'Bounded':
            return False 
        return True 
                    

