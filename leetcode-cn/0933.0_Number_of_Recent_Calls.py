'''
执行用时：212 ms, 在所有 Python3 提交中击败了89.36% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了45.46% 的用户
通过测试用例：68 / 68
'''
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


'''
执行用时：208 ms, 在所有 Python3 提交中击败了94.96% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了81.97% 的用户
通过测试用例：68 / 68
'''
class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
