'''
执行用时：60 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：19.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：64 / 64
'''
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        M = len(rolls)
        sumn = mean * (n + M) - sum(rolls)
        if sumn < n or sumn > n * 6:
            return []
        avg, remainder = divmod(sumn, n)
        return [avg + 1] * remainder + [avg] * (n - remainder)
        