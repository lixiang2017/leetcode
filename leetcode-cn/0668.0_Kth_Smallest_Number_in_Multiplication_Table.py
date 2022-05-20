'''
binary search, T: O(min(M,N)log(MN)), S: O(1)

执行用时：596 ms, 在所有 Python3 提交中击败了85.96% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了77.19% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m
        
        def enough(val):
            cnt = 0
            for row in range(1, m + 1):
                cnt += min(n, val // row)
            return cnt >= k
        
        lo, hi, kth = 1, m * n, 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if enough(mid):
                kth = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return kth 



'''
输入：
45
12
471
输出：
311
预期结果：
312

In [3]: s = sorted([i * j for i in range(1, 46) for j in range(1, 13)])
In [4]: s
...
 308,
 310,
 312,
 312,
 315,
...
有多个312，所以check(mid)的时候，需要cnt>=k在一起，也就是>和=需要是同一个判断结果。
'''

'''
binary search, T: O(min(M,N)log(MN)), S: O(1)

执行用时：688 ms, 在所有 Python3 提交中击败了79.44% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了97.78% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        ans = 0
        # l, r = 1, m * n 
        l, r = 0, m * n
        if m > n:
            m, n = n, m

        def check(x):
            cnt = 0
            # every row
            for i in range(1, m + 1):
                cnt += min(x // i, n) 
                if cnt >= k:
                    return False 
            return True

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                # mid is too large, or mid is just answer
                ans = mid 
                r = mid - 1
        
        return ans 




'''
执行用时：952 ms, 在所有 Python3 提交中击败了15.00% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了7.22% 的用户
通过测试用例：70 / 70
'''
class Solution(Sequence):

    def __len__(self):
        return self.m * self.n

    def __getitem__(self, item):
        return sum([min(item // i, self.n) for i in range(1, self.m + 1)])

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        self.m = m 
        self.n = n 
        return bisect_left(self, k)


'''
https://github.com/python/cpython/blob/3.9/Lib/bisect.py
https://github.com/python/cpython/blob/3.10/Lib/bisect.py

执行用时：256 ms, 在所有 Python3 提交中击败了91.67% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了92.78% 的用户
通过测试用例：70 / 70
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n + 1), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))
