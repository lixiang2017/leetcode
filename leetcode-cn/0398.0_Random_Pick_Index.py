'''
执行用时：92 ms, 在所有 Python3 提交中击败了45.43% 的用户
内存消耗：25.8 MB, 在所有 Python3 提交中击败了5.22% 的用户
通过测试用例：14 / 14
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.num2indice = defaultdict(list)
        for i, x in enumerate(nums):
            self.num2indice[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.num2indice[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)



'''
执行用时：104 ms, 在所有 Python3 提交中击败了30.87% 的用户
内存消耗：24.9 MB, 在所有 Python3 提交中击败了16.95% 的用户
通过测试用例：14 / 14
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.num2indice = defaultdict(list)
        for i, x in enumerate(nums):
            self.num2indice[x].append(i)

    def pick(self, target: int) -> int:
        n = len(self.num2indice[target])
        return self.num2indice[target][random.randint(0, 10 ** 9 + 7) % n]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
