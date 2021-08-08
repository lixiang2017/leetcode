'''
Stack + Two Pointers

58 / 58 个通过测试用例
状态：通过
执行用时: 1064 ms
内存消耗: 26.2 MB
提交时间：5 小时前
'''


class Solution:
    def minSwaps(self, s: str) -> int:
        N = len(s)
        l, r = 0, N - 1
        # left stack, right stack
        lstk, rstk = [], []
        swap = 0
        while l < r:
            while True:
                pre_l = l
                while l < N and s[l] == '[':
                    lstk.append(s[l])
                    l += 1
                while  l < N and s[l] == ']' and lstk:
                    lstk.pop()
                    l += 1
                if l == pre_l:
                    break    
                
            while True:   
                pre_r = r
                while r >= 0 and s[r] == ']':
                    rstk.append(s[r])
                    r -= 1
                while r >= 0 and s[r] == '[' and rstk:
                    rstk.pop()
                    r -= 1
                if r == pre_r:
                    break    
                    
            if l < r:   
                swap += 1
            #
            lstk.append('[')
            rstk.append(']')
            #
            l += 1
            r -= 1
            
        return swap

'''
"][]["
"]]][[["
"[]"
"]]]][[[["
"]]]]][[[[[" 

输入：
"][[]][][[][]"
输出：
2
预期：
1
'''

