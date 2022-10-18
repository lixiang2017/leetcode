'''
simulation

执行用时：40 ms, 在所有 Python3 提交中击败了48.32% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了92.66% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        dn = len(digits)
        nl, nn = 0, n 
        while nn:
            nl += 1
            nn //= 10
        ans = 0
        for i in range(1, nl):
            ans += dn ** i
        
        while n > 0:
            first = n // (10 ** (nl - 1))
            if nl > 1:
                le_cnt = sum(int(ch) < first for ch in digits)
                ans += le_cnt * dn ** (nl - 1)
            else:
                ans += sum(int(ch) <= n for ch in digits)
                break
            if le_cnt < dn and int(digits[le_cnt]) == first:
                n -= first * (10 ** (nl - 1))
                nl -= 1
            else:
                break 

        return ans 
