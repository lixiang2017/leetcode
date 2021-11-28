'''
60 / 60 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 15.3 MB
提交时间：1 天前
'''
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans = 0
        c1, c2 = Counter(words1), Counter(words2)
        for k1, v1 in c1.items():
            if v1 == 1 and k1 in c2 and c2[k1] == 1:
                ans += 1
        
        return ans
