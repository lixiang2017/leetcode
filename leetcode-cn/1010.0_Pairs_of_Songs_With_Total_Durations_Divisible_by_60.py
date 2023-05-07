'''
执行用时：68 ms, 在所有 Python3 提交中击败了68.52% 的用户
内存消耗：19.7 MB, 在所有 Python3 提交中击败了5.56% 的用户
通过测试用例：35 / 35
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = Counter(t % 60 for t in time)
        ans = c[0] * (c[0] - 1) // 2 + c[30] * (c[30] - 1) // 2
        for r in range(1, 30):
            ans += c[r] * c[60 - r]
        return ans
        