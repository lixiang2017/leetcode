'''
数位DP，T:O(logN),S:O(1)

执行用时：32 ms, 在所有 Python3 提交中击败了84.25% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了55.12% 的用户
'''
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        base = 1
        ans = 0
        while n >= base:
            # digit
            d = n // base % 10
            # high
            ans += n // (base * 10) * base
            # left
            if d <= 1:
                ans += 0
            elif d == 2:
                ans += n % base + 1
            else:
                ans += base

            base *= 10
        
        return ans

