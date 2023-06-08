'''
执行用时：252 ms, 在所有 Python3 提交中击败了16.64% 的用户
内存消耗：36.1 MB, 在所有 Python3 提交中击败了23.19% 的用户
通过测试用例：564 / 564
'''
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [(r2 - r1, i) for i, (r1, r2) in enumerate(zip(reward1, reward2))]
        diff.sort()
        return sum(reward1[diff[i][1]] for i in range(k)) + sum(reward2[diff[i][1]] for i in range(k, n))
        