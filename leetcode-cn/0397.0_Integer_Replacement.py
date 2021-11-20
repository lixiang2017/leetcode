'''
BFS

执行用时：68 ms, 在所有 Python3 提交中击败了50.00% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.19% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def integerReplacement(self, n: int) -> int:
        q = deque([(n, 0)])
        while True:
            x, step = q.popleft()
            if x == 1:
                return step
            if x % 2 == 0:
                q.append((x // 2, step + 1))
            else:
                q.append((x + 1, step + 1))
                q.append((x - 1, step + 1))


'''
BFS + Hash Set

执行用时：28 ms, 在所有 Python3 提交中击败了94.81% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.26% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def integerReplacement(self, n: int) -> int:
        q = deque([(n, 0)])
        seen = set()
        while True:
            x, step = q.popleft()
            if x == 1:
                return step
            seen.add(x)
            if x % 2 == 0:
                if x // 2 not in seen:
                    q.append((x // 2, step + 1))
            else:
                for nx in [x + 1, x - 1]:
                    if nx not in seen:
                        q.append((nx, step + 1))

