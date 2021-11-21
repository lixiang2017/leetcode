'''
执行用时：152 ms, 在所有 Python3 提交中击败了78.59% 的用户
内存消耗：20.3 MB, 在所有 Python3 提交中击败了62.28% 的用户
通过测试用例：10 / 10
'''
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        nums = self.origin[:]
        random.shuffle(nums)
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
