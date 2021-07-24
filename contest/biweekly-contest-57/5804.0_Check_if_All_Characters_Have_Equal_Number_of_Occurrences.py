'''
132 / 132 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 15 MB
提交时间：2 小时前
'''
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = Counter(s)
        return len(set(cnt.values())) == 1

