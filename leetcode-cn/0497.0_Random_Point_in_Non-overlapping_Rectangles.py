'''
千万记住是点的个数，不是面积
所以要使用(x - a + 1) * (y - b + 1)，而非(x - a) * (y - b)

执行用时：148 ms, 在所有 Python3 提交中击败了72.08% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了70.78% 的用户
通过测试用例：35 / 35
'''
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.points = 0
        self.pre = []
        for a, b, x, y in rects:
            self.points += (x - a + 1) * (y - b + 1)
            self.pre.append(self.points)

    def pick(self) -> List[int]:
        a = random.randint(0, self.points)
        idx = bisect_left(self.pre, a)
        a, b, x, y = self.rects[idx]
        return [randint(a, x), randint(b, y)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
