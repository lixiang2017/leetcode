'''
每次选择最大的，逐渐减小。这种贪心是错误的。反例：
12 = 9 + 1 + 1 + 1   4次
12 = 4 + 4 + 4       3次
所以DP

T: O(N * sqrt(N) = N^1.5)
S: O(N)

执行用时：7132 ms, 在所有 Python3 提交中击败了5.00% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了22.55% 的用户
通过测试用例：588 / 588
'''

class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))
        i = 1
        while i * i <= n:
            square = i * i 
            for j in range(1, n + 1):
                fold, remainder = divmod(j, square)
                dp[j] = min(dp[j], dp[remainder] + fold)

            i += 1
        
        return dp[n]


'''
from i = 2, from j = square

执行用时：4768 ms, 在所有 Python3 提交中击败了26.20% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了24.13% 的用户
通过测试用例：588 / 588
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))
        i = 2
        while i * i <= n:
            square = i * i 
            for j in range(square, n + 1):
                fold, remainder = divmod(j, square)
                dp[j] = min(dp[j], dp[remainder] + fold)

            i += 1
        
        return dp[n]


'''
from i = 2, from j = square, 计算一次square

执行用时：4488 ms, 在所有 Python3 提交中击败了32.90% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了33.36% 的用户
通过测试用例：588 / 588
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))
        i, square = 2, 4
        while square <= n:
            for j in range(square, n + 1):
                fold, remainder = divmod(j, square)
                dp[j] = min(dp[j], dp[remainder] + fold)

            i += 1
            square = i * i 
        return dp[n]

'''
外层是i,内层是平方和

执行用时：4820 ms, 在所有 Python3 提交中击败了25.34% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了75.00% 的用户
通过测试用例：588 / 588
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = i 
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


'''
最后赋值 dp[i] = minx + 1

执行用时：4248 ms, 在所有 Python3 提交中击败了40.66% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了60.90% 的用户
通过测试用例：588 / 588
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            minx, j = i, 1
            while j * j <= i:
                minx = min(minx, dp[i - j * j])
                j += 1
            dp[i] = minx + 1
        return dp[n]


'''
四平方定理
四平方和定理证明了任意一个正整数都可以被表示为至多四个正整数的平方和。
1、任何正整数都可以拆分成不超过4个数的平方和 ---> 答案只可能是1,2,3,4
2、如果一个数最少可以拆成4个数的平方和，则这个数还满足 n = (4^a)*(8b+7) 
---> 因此可以先看这个数是否满足上述公式，如果不满足，答案就是1,2,3了
3、如果这个数本来就是某个数的平方，那么答案就是1，否则答案就只剩2,3了
4、如果答案是2，即n=a^2+b^2，那么我们可以枚举a，来验证，如果验证通过则答案是2
5、只能是3

T: O(logN + N^0.5)
S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了97.84% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了71.52% 的用户
通过测试用例：588 / 588
'''
class Solution:
    # answer just in 1 2 3 4
    def numSquares(self, n: int) -> int:
        def isPerfectSquare(x):
            y = int(sqrt(x))
            return y * y == x
        
        def isAnswer4(x):
            # 4^k * (8*k+7)
            while x % 4 == 0:
                x //= 4
            return x % 8 == 7
        
        if isPerfectSquare(n):
            return 1
        elif isAnswer4(n):
            return 4
        for i in range(1, int(sqrt(n)) + 1):
            j = n - i * i
            if isPerfectSquare(j):
                return 2
        return 3

'''
BFS

执行用时：452 ms, 在所有 Python3 提交中击败了86.85% 的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了5.01% 的用户
通过测试用例：588 / 588
'''
class Solution:
    def numSquares(self, n: int) -> int:
        # (x, step)
        q = deque([(n, 0)])
        seen = set()
        while q:
            x, step = q.popleft()
            targets = [x - i * i for i in range(1, int(sqrt(n)) + 1)]
            for t in targets:
                if t == 0:
                    return step + 1
                if t not in seen:
                    seen.add(t)
                    q.append((t, step + 1))
        return -1




