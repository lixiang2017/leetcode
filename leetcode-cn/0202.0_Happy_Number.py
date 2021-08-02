'''
Hash Set + divmod

执行用时：28 ms, 在所有 Python3 提交中击败了98.60% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了17.20% 的用户
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        if 1 == n:
            return True
        seen = {n}
        
        def trans(x: int):
            h = 0
            while x:
                x, r = divmod(x, 10)
                h += r * r
            return h

        while True:
            nn = trans(n)
            if nn == 1:
                return True
            elif nn in seen:
                return False
            seen.add(nn)
            n = nn
            
        return False
