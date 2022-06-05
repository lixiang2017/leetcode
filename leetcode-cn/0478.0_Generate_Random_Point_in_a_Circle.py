'''
在圆的外接正方形内随机，判断在圆外部的时候重新随机即可。
factor

执行用时：152 ms, 在所有 Python3 提交中击败了89.82% 的用户
内存消耗：24.9 MB, 在所有 Python3 提交中击败了51.33% 的用户
通过测试用例：8 / 8
'''
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius 
        self.x = x_center 
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            f1 = (random.random() - 0.5) * 2
            f2 = (random.random() - 0.5) * 2
            dx = self.r * f1
            dy = self.r * f2
            if dx * dx + dy * dy <= self.r * self.r:
                return [self.x + dx, self.y + dy]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()


'''
执行用时：148 ms, 在所有 Python3 提交中击败了96.02% 的用户
内存消耗：24.9 MB, 在所有 Python3 提交中击败了57.96% 的用户
通过测试用例：8 / 8
'''
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius 
        self.x = x_center 
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            f1 = (random.random() - 0.5) * 2
            f2 = (random.random() - 0.5) * 2
            if f1 * f1 + f2 * f2 <= 1:
                return [self.x + self.r * f1, self.y + self.r * f2]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()



'''
In [12]: ??random.uniform
Signature: random.uniform(a, b)
Source:
    def uniform(self, a, b):
        "Get a random number in the range [a, b) or [a, b] depending on rounding."
        return a + (b-a) * self.random()
File:      /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/random.py
Type:      method


执行用时：176 ms, 在所有 Python3 提交中击败了36.73% 的用户
内存消耗：24.7 MB, 在所有 Python3 提交中击败了95.58% 的用户
通过测试用例：8 / 8
'''
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius 
        self.x = x_center 
        self.y = y_center

    def randPoint(self) -> List[float]:
        nx = random.uniform(self.x - self.r, self.x + self.r)
        ny = random.uniform(self.y - self.r, self.y + self.r)
        while (nx - self.x) ** 2 + (ny - self.y) ** 2 > self.r ** 2:
            nx = random.uniform(self.x - self.r, self.x + self.r)
            ny = random.uniform(self.y - self.r, self.y + self.r) 
        return [nx, ny]           

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()


'''
执行用时：144 ms, 在所有 Python3 提交中击败了97.35% 的用户
内存消耗：24.8 MB, 在所有 Python3 提交中击败了82.74% 的用户
通过测试用例：8 / 8
'''
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius 
        self.x = x_center 
        self.y = y_center

    def randPoint(self) -> List[float]:
        u, theta = random.random(), random.random() * 2 * math.pi
        f = sqrt(u)
        return [self.x + f * self.r * math.cos(theta), self.y + f * self.r * math.sin(theta)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()




