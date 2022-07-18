'''
35 / 80 个通过测试用例
状态：超出时间限制
提交时间：几秒前
最后执行的输入：
1000
1000
'''
class Solution:
    MOD = 10 ** 9 + 7

    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if k < 0:
            return 0 
        if 1 == n:
            if k >= 1:
                return 0
            return 1
        if 2 == n:
            if k < 2:
                return 1
            else:
                return 0
        c = 0
        for j in range(k, k - n, -1):
            c += self.kInversePairs(n - 1, j)
        return c % self.MOD 


'''
DFS, 递推公式 + 错位相减化简递推公式

f(n,k) = f(n-1,k) + f(n-1,k-1) + f(n-1,k-2) + f(n-1,k-3) + ... + f(n-1,k-n+1)
=>
f(n,k+1) = f(n-1,k+1) + f(n-1,k-1) + f(n-1,k-2) + ... + f(n-1,k-n+2)
=>
f(n,k+1) - f(n,k) = f(n-1,k+1) - f(n-1,k-n+1)
=>
f(n,k+1) = f(n,k) + f(n-1,k+1) - f(n-1,k-n+1)
=>
f(n,k) = f(n,k-1) + f(n-1,k) - f(n-1,k-n)

两个递推公式：

    f(n,k) = f(n-1,k)+f(n-1,k-1) + f(n-1,k-2) + f(n-1,k-3) + ... + f(n-1,k-n+1)
    f(n,k) = f(n,k-1) + f(n-1,k) - f(n-1,k-n)

T: O(NK)
S: O(NK)

执行用时：3436 ms, 在所有 Python3 提交中击败了6.06% 的用户
内存消耗：392.9 MB, 在所有 Python3 提交中击败了6.06% 的用户
通过测试用例：80 / 80
'''
class Solution:
    MOD = 10 ** 9 + 7

    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if k < 0:
            return 0 
        if 1 == n:
            if k >= 1:
                return 0
            else:
                return 1
        if 2 == n:
            if k < 2:
                return 1
            else:
                return 0
        c = 0
        c += self.kInversePairs(n, k - 1)
        c += self.kInversePairs(n - 1, k)
        c -= self.kInversePairs(n - 1, k - n)
        return c % self.MOD 



'''
no need to write 2 == n

执行用时：3468 ms, 在所有 Python3 提交中击败了6.06% 的用户
内存消耗：393.2 MB, 在所有 Python3 提交中击败了6.06% 的用户
通过测试用例：80 / 80
'''
class Solution:
    MOD = 10 ** 9 + 7

    @cache
    def kInversePairs(self, n: int, k: int) -> int:
        if k < 0:
            return 0 
        if 1 == n:
            if k >= 1:
                return 0
            else:
                return 1
        c = 0
        c += self.kInversePairs(n, k - 1)
        c += self.kInversePairs(n - 1, k)
        c -= self.kInversePairs(n - 1, k - n)
        return c % self.MOD 


