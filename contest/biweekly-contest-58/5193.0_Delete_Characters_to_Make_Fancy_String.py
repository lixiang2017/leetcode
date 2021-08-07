'''
类似Moore投票法

306 / 306 个通过测试用例
状态：通过
执行用时: 280 ms
内存消耗: 16.6 MB
提交时间：2 小时前
'''
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans, cnt = [], 0
        pre = ''
        for c in s:
            if c == pre:
                cnt += 1
                if cnt < 3:
                    ans.append(c)
            else:
                pre = c
                cnt = 1
                ans.append(c)
                
        return ''.join(ans)
