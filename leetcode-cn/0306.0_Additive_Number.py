'''
执行用时：32 ms, 在所有 Python3 提交中击败了78.52% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了86.24% 的用户
通过测试用例：42 / 42
'''
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # 7 0 7 7 14 21
        # 1 0 1 1 2 3 5
        # 0 6 6 12 18 30 48
        n = len(num)
        if n < 3:
            return False
        
        def check(x1, x2, idx):
            if idx == n:
                return True 
            x12 = x1 + x2 
            sx12 = str(x12)
            if idx + len(sx12) > n:
                return False 
            if num[idx: idx + len(sx12)] != sx12:
                return False 
            else:
                return check(x2, x12, idx + len(sx12))

        def leading_zero(x, x_len):
            if x == 0 and x_len == 1:
                return False 
            if x_len > 1 and len(str(x)) != x_len:
                return True 
            return False 

        for i in range(n // 2):
            x1 = int(num[: i + 1])
            if leading_zero(x1, i + 1):
                continue
            for j in range(i + 2, n):
                x2 = int(num[i + 1: j])
                if leading_zero(x2, j - i - 1):
                    continue
                if check(x1, x2, j):
                    return True
        
        return False 

