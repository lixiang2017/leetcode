'''
执行用时：52 ms, 在所有 Python3 提交中击败了8.05% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了71.26% 的用户
通过测试用例：215 / 215
'''
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        nl = len(n)
        int_n = int(n)
        ans = '0'

        def isCloser(int_cand, ans):
            if int_cand == int_n:
                return False
            return abs(int_cand - int_n) < abs(int(ans) - int_n) or \
                    (abs(int_cand - int_n) == abs(int(ans) - int_n) and int_cand < int(ans))

        if nl % 2:
            left_part = n[: nl//2] 
            cand1 = left_part + n[nl//2] + left_part[:: -1]
            int_cand1 = int(cand1)
            if isCloser(int_cand1, ans):
                ans = cand1
            if n[nl//2] != '9':
                more1 = str(int(n[nl//2]) + 1)
                cand2 = left_part + more1 + left_part[:: -1]
                int_cand2 = int(cand2)
                if isCloser(int_cand2, ans):
                    ans = cand2 
            if  n[nl//2] != '0':
                less1 = str(int(n[nl//2]) - 1)
                cand3 = left_part + less1 + left_part[:: -1]
                int_cand3 = int(cand3)
                if isCloser(int_cand3, ans):
                    ans = cand3           
        else:
            left_part = n[: nl//2] 
            cand1 = left_part + left_part[:: -1]
            int_cand1 = int(cand1)
            if isCloser(int_cand1, ans):
                ans = cand1        
            # more 1
            left_part = str(int(n[: nl//2] ) + 1)
            cand2 = left_part + left_part[:: -1]
            int_cand2 = int(cand2)
            if isCloser(int_cand2, ans):
                ans = cand2 
            # less 1
            left_part = str(int(n[: nl//2]) - 1)
            cand3 = left_part + left_part[:: -1]
            int_cand3 = int(cand3)
            if isCloser(int_cand3, ans):
                ans = cand3       

        for cand in [int_n - 2, int_n - 1, int_n + 1, int_n + 2]:
            s_cand = str(cand)
            if s_cand == s_cand[:: -1] and isCloser(cand, ans):
                ans = s_cand

        return ans 

'''
"100000000000001"
"1000000000001"
"101"
"1001"
"10"
"100"
"1000000"
"99"
'''




