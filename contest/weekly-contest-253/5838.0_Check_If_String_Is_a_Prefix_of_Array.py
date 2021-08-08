'''
346 / 346 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 15.1 MB
提交时间：6 小时前
'''
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(len(words) + 1):
            if s == ''.join(words[:i]):
                return True
        
        return False
        