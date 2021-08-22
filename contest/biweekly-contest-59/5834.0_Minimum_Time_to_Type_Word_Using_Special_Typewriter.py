'''
134 / 134 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 15 MB
提交时间：1 天前
'''

class Solution:
    def minTimeToType(self, word: str) -> int:
        N = len(word)
        total = 0
        for i in range(N):
            if 0 == i:
                total += min(ord(word[i]) - ord('a'), ord('z') - ord(word[i]) + 1)
            else:
                m1 = abs(ord(word[i]) - ord(word[i-1]))
                total += min(m1, 26 - m1)
        
        return total + N
