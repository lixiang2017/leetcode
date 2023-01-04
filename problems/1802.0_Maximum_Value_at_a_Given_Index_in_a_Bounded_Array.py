'''
binary search
如果弄不清楚是需要 +1 还是 -1，是 谁+谁 还是谁-谁，就在草稿纸上用几个例子实验一下。 
4个例子足够说明问题。

执行用时：48 ms, 在所有 Python3 提交中击败了40.91% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了86.36% 的用户
通过测试用例：370 / 370
'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def check(m):
            # try to set nums[index] = m
            total = 0
            # from left to m
            left = max(m - index, 1)
            total += (left + m) * (m - left + 1) // 2
            ## left
            total += max(index - m + 1, 0)
            # from m-1 to right
            right = max(m - (n - index) + 1, 1)
            total += (m - 1 + right) * (m - 1 - right + 1) // 2
            ## right
            total += max(n - index - m, 0)
            return total <= maxSum 
        
        l, r = 1, maxSum
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
