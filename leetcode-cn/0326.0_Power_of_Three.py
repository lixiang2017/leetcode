'''
approach: Loop Iteration
Time: O(logN)
Space: O(1)


执行结果：
通过
显示详情
执行用时：168 ms, 在所有 Python 提交中击败了88.33%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了5.00%的用户
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        
        while n:
            if n == 1: return True
            if n % 3: return False
            n /= 3

        return True



'''
执行用时：92 ms, 在所有 Python3 提交中击败了33.24% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.70% 的用户
通过测试用例：21038 / 21038
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                return False
        return 1 == n


'''
执行用时：84 ms, 在所有 Python3 提交中击败了48.23% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了77.06% 的用户
通过测试用例：21038 / 21038
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        x = 1
        while x < n:
            x *= 3
        return x == n


'''
执行用时：72 ms, 在所有 Python3 提交中击败了77.35% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了47.17% 的用户
通过测试用例：21038 / 21038
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n and n % 3 == 0:
            n //= 3
        return 1 == n


'''
执行用时：72 ms, 在所有 Python3 提交中击败了77.35% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了65.23% 的用户
通过测试用例：21038 / 21038
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0



'''
执行用时：60 ms, 在所有 Python3 提交中击败了96.36% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了86.16% 的用户
通过测试用例：21038 / 21038
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        p3 = set([1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467])
        return n in p3


'''
执行用时：72 ms, 在所有 Python3 提交中击败了77.35% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了94.44% 的用户
通过测试用例：21038 / 21038
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        p3 = [1,
            3,
            9,
            27,
            81,
            243,
            729,
            2187,
            6561,
            19683,
            59049,
            177147,
            531441,
            1594323,
            4782969,
            14348907,
            43046721,
            129140163,
            387420489,
            1162261467]
        return n in p3



'''
Recursion

执行用时：64 ms, 在所有 Python3 提交中击败了92.05% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了14.03% 的用户
通过测试用例：21038 / 21038
'''
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        elif 1 == n: return True
        elif n % 3: return False
        else:
            return self.isPowerOfThree(n // 3)

