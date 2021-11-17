'''
Binary Search
T: O(Mlog(MN))
S: O(1)

Runtime: 892 ms, faster than 68.80% of Python3 online submissions for Kth Smallest Number in Multiplication Table.
Memory Usage: 14.3 MB, less than 29.25% of Python3 online submissions for Kth Smallest Number in Multiplication Table.

ref:
https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/comments/

            // 乘法表的性质 也就是O(1)时间能算出来每行比num小的数的个数
            // 而第378题 每次检验需要O(m + n)
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m * n
        ans = 1
        while lo <= hi:
            target = (lo + hi) // 2
            cnt = self.countLowerTarget(m, n, target)
            if cnt < k:
                lo = target + 1
            else:
                ans = target
                hi = target - 1
                
        return ans
    
    def countLowerTarget(self, m: int, n: int, target: int) -> int:
        cnt = 0
        for row in range(1, m + 1):
            cnt += min(n, target // row)
        return cnt


'''
Binary Search
T: O(min(M, N) * log(MN))
S: O(1)

Runtime: 708 ms, faster than 94.99% of Python3 online submissions for Kth Smallest Number in Multiplication Table.
Memory Usage: 14.2 MB, less than 62.67% of Python3 online submissions for Kth Smallest Number in Multiplication Table.
'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m * n
        ans = 1
        while lo <= hi:
            target = (lo + hi) // 2
            cnt = self.countLowerTarget(m, n, target)
            if cnt < k:
                lo = target + 1
            else:
                ans = target
                hi = target - 1
                
        return ans
    
    def countLowerTarget(self, m: int, n: int, target: int) -> int:
        cnt = 0
        if m <= n:
            for row in range(1, m + 1):
                cnt += min(n, target // row)
        else:
            for col in range(1, n + 1):
                cnt += min(m, target // col)
        return cnt

