'''
多次采样

执行用时：64 ms, 在所有 Python3 提交中击败了14.43% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了59.79% 的用户
通过测试用例：20 / 20
'''
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.seen = set()

    def flip(self) -> List[int]:
        while True:
            x = random.randint(0, self.m - 1)
            y = random.randint(0, self.n - 1)
            if (x, y) not in self.seen:
                self.seen.add((x, y))
                return [x, y]

    def reset(self) -> None:
        self.seen = set()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()



'''
多次采样

执行用时：56 ms, 在所有 Python3 提交中击败了32.65% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了79.59% 的用户
通过测试用例：20 / 20
'''
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.seen = set()

    def flip(self) -> List[int]:
        while (x := random.randint(0, self.m * self.n - 1)) in self.seen:
            pass
        self.seen.add(x)
        return divmod(x, self.n)
        
    def reset(self) -> None:
        self.seen.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()


'''
单次采样

ref:
https://leetcode-cn.com/problems/random-flip-matrix/solution/mo-gu-qie-cha-duo-ci-cai-yang-dan-ci-cai-biq9/

执行用时：40 ms, 在所有 Python3 提交中击败了94.90% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了47.96% 的用户
通过测试用例：20 / 20
'''
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.map = dict()
        self.total = m * n

    def flip(self) -> List[int]:
        self.total -= 1
        x = random.randint(0, self.total)
        idx = self.map.get(x, x)
        self.map[x] = self.map.get(self.total, self.total)
        return divmod(idx, self.n)

    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()








