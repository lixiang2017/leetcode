'''
81 / 81 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 15 MB
提交时间：5 小时前
'''
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 if p in word else 0 for p in patterns])
        