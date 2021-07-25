'''
216 / 216 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 15.1 MB
提交时间：1 小时前
'''
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ''.join([str(ord(ch) - ord('a') + 1) for ch in s])
        total = sum(int(ch) for ch in ss)
        next_total = 0
        while k > 1:
            while total:
                next_total += total % 10
                total //= 10
            next_total, total = total, next_total
            k -= 1
        return total
