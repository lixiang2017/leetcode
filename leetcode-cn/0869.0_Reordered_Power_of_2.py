'''
执行用时：36 ms, 在所有 Python3 提交中击败了67.07% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了19.16% 的用户
通过测试用例：136 / 136
'''
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers = [2 ** i for i in range(30)]
        ps = set(''.join(sorted(list(str(p)))) for p in powers)
        return ''.join(sorted(list(str(n)))) in ps
        