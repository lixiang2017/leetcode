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
