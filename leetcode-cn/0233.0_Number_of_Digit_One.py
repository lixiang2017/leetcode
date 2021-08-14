'''
数位DP
T:O(logN),S:O(1)

执行用时：24 ms, 在所有 Python3 提交中击败了97.44% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了51.03% 的用户
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        base = 1
        while n >= base:
            # from lowest to highest, bit(decimal)
            b = n // base % 10
            if b < 1:
                ans += n // (base * 10) * base
            elif 1 == b:
                ans += n // (base * 10) * base + n % base + 1
            else:
                ans += n // (base * 10) * base + base
            base *= 10

        return ans


'''
执行用时：16 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.74% 的用户
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        base = 1
        while n >= base:
            # from lowest to highest, bit(decimal)
            b = n // base % 10
            ans += n // (base * 10) * base + \
                min(max(n % (base * 10) - base + 1, 0), base)
            base *= 10

        return ans
