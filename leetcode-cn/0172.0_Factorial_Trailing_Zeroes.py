'''
T:O(logN),S:O(1)
只需要计算有多少个5

执行用时：40 ms, 在所有 Python3 提交中击败了57.59% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.48% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        i = 5
        while i <= n:
            cnt += n // i
            i *= 5
        return cnt


'''
执行用时：40 ms, 在所有 Python3 提交中击败了59.39% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了35.71% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 2 4 6 8 10 12 14 
        # 5 10 15 20 25 30 35 40 45 50 55 60 ... 125  (5) 
        # 25 50 75 100   (5 * 5)   //5 -> 5 10 15 20

        # 5以内    1
        # 25以内   6
        # 125以内  1-25 6 26-50 6 51-75 6 76-100 6  100-125 6+1
        ans = 0
        pre, cnt = 1, 0
        while pre <= n:
            ans = cnt 
            cnt = cnt * 5 + 1
            pre *= 5

        pre //= 5
        # 还剩下的区间长度
        n -= pre 
        while n > 0:
            cnt = (cnt - 1) // 5
            ans += n // pre * cnt 
            n %= pre
            pre //= 5
        return ans 


'''
执行用时：32 ms, 在所有 Python3 提交中击败了90.25% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了69.96% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        div, ans = 5, 0
        while div <= n:
            ans += n // div
            div *= 5
        return ans 


'''
recursive
执行用时：40 ms, 在所有 Python3 提交中击败了59.84% 的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了97.46% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n // 5 + (self.trailingZeroes(n // 5) if n  else 0)


'''
执行用时：40 ms, 在所有 Python3 提交中击败了59.84% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了90.98% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans 


'''
执行用时：28 ms, 在所有 Python3 提交中击败了96.79% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了43.31% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return n // 5 + n // 25 + n // 125 + n // 625 + n // 3125


'''
执行用时：24 ms, 在所有 Python3 提交中击败了99.52% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了56.81% 的用户
通过测试用例：500 / 500
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        for i in (5, 25, 125, 625, 3125):
            ans += n // i
        return ans 


        


