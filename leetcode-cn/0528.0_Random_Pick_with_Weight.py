'''
Prefix Sum + Binary Search

执行用时：172 ms, 在所有 Python3 提交中击败了86.25% 的用户
内存消耗：19.3 MB, 在所有 Python3 提交中击败了69.17% 的用户
通过测试用例：57 / 57
'''
class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = self.pre[-1]

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect.bisect_left(self.pre, x)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
