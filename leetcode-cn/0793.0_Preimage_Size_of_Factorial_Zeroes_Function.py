'''
Binary Search

执行用时：28 ms, 在所有 Python3 提交中击败了90.32% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了84.68% 的用户
通过测试用例：44 / 44
'''
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        lower = self.getLower(k)
        upper = self.getUpper(k, lower)
        return upper - lower + 1 if lower != -1 else 0
    
    def getLower(self, k: int) -> int:
        l, r = 0, 5 * 10**9
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            zero = self.trailingZeros(mid)
            if zero > k:
                r = mid - 1
            elif zero < k:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans

    def getUpper(self, k: int, lower: int) -> int:
        l, r = lower, 5 * 10**9
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            zero = self.trailingZeros(mid)
            if zero > k:
                r = mid - 1
            elif zero < k:
                l = mid + 1
            else:
                ans = mid
                l = mid + 1
        return ans

    def trailingZeros(self, n: int) -> int:
        cnt = 0
        i = 5
        while i <= n:
            cnt += n // i
            i *= 5
        return cnt



'''
执行用时：28 ms, 在所有 Python3 提交中击败了90.32% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.64% 的用户
通过测试用例：44 / 44
'''
    def getUpper(self, k: int, lower: int) -> int:
        if -1 == lower:
            return -1
            
        l, r = lower, 5 * 10**9
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            zero = self.trailingZeros(mid)
            if zero > k:
                r = mid - 1
            elif zero < k:
                l = mid + 1
            else:
                ans = mid
                l = mid + 1
        return ans



'''
binary search

执行用时：52 ms, 在所有 Python3 提交中击败了10.68% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了72.95% 的用户
通过测试用例：44 / 44
'''
class Solution:

    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans 

    def preimageSizeFZF(self, k: int) -> int:
        left = self.findLeft(k)
        right = self.findRight(k)
        return right - left + 1

    def findLeft(self, k: int) -> int:
        low = 0
        high = 10 ** 10
        while low <= high:
            mid = (low + high) // 2
            c = self.trailingZeroes(mid)
            if c > k:
                high = mid - 1
            elif c < k:
                low = mid + 1
            else:
                high = mid - 1
        return high + 1
        
    def findRight(self, k: int) -> int:
        low = 0
        high = 10 ** 10
        while low <= high:
            mid = (low + high) // 2
            c = self.trailingZeroes(mid)
            if c > k:
                high = mid - 1
            elif c < k:
                low = mid + 1
            else:
                low = mid + 1
        return low - 1


'''
In [7]: Solution().trailingZeroes(10 ** 10)
Out[7]: 2499999997

In [8]: Solution().trailingZeroes(10 ** 9)
Out[8]: 249999998
'''

