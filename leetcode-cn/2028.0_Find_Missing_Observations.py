'''
simulation

执行用时：100 ms, 在所有 Python3 提交中击败了71.60% 的用户
内存消耗：19.6 MB, 在所有 Python3 提交中击败了25.92% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        left = mean * (m + n) - sum(rolls)
        # if left < 0 or left > 6 * n:  # wrong, can not be less than one for each
        if left < n or left > 6 * n:
            return []
        avg, r = divmod(left, n)
        return [avg + 1] * r +  [avg] * (n - r)
