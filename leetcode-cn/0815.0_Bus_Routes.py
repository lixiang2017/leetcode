'''
Hash Set + BFS

43 / 45 个通过测试用例
状态：超出时间限制
提交时间：2 分钟内
'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        q = deque()
        seen = set()  # seen route

        # for route in routes:
        for i in range(len(routes)):
            if source in routes[i]:
                for station in routes[i]:
                    if station == target:
                        return 1
                    q.append((station, 1))   # (station, step)
                seen.add(i)
        
        while q:
            station, step = q.popleft()
            #if station == target:
            #    return step
            for i in range(len(routes)):
                if i not in seen and station in routes[i]:
                    for s in routes[i]:
                        if s == target:
                            return step + 1
                        q.append((s, step + 1))
                    seen.add(i)

        return -1

'''
输入：
[[1,7],[3,5]]
5
5
输出：
1
预期结果：
0
'''



'''
Hash Set + Hash Set + BFS

执行用时：1484 ms, 在所有 Python3 提交中击败了15.31% 的用户
内存消耗：29 MB, 在所有 Python3 提交中击败了45.15% 的用户
'''
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        routes = [set(route) for route in routes]
        q = deque()
        seen = set()  # seen route
        for i in range(len(routes)):
            if source in routes[i]:
                for station in routes[i]:
                    if station == target:
                        return 1
                    q.append((station, 1))   # (station, step)
                seen.add(i)
        
        while q:
            station, step = q.popleft()
            for i in range(len(routes)):
                if i not in seen and station in routes[i]:
                    for s in routes[i]:
                        if s == target:
                            return step + 1
                        q.append((s, step + 1))
                    seen.add(i)

        return -1