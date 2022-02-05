'''
DFS

执行用时：148 ms, 在所有 Python3 提交中击败了5.41% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.40% 的用户
通过测试用例：504 / 504
'''
'''
1: 1
2: 2
3: 3
4: 2 + 2, 1 + 3
5: 5
6: 1 + 5, 3 + 3
7: 2 + 5
8: 8
9: 1 + 8
10: 2 + 8
11: 3 + 8
'''

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        a = b = 1
        while b <= k:
            a, b = b, a + b
            fib.append(b)
        
        @lru_cache(None)
        def count(x, cnt, pos):
            if x == 0:
                return cnt 
            idx = bisect_left(fib, x)
            ans = float('inf')
            for i in range(idx, -1, -1):
                if i >= pos:
                    break
                if x >= fib[i]:
                    ans = min(ans, count(x - fib[i], cnt + 1, i))
            return ans

        return count(k, 0, float('inf'))


