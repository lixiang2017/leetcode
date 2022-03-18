'''
binary search
T: O(N * log(sum(nums) - max(nums)))
S: O(1)

执行用时：28 ms, 在所有 Python3 提交中击败了97.44% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了39.91% 的用户
通过测试用例：30 / 30
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def check(target) -> bool:
            cnt = 1
            _sum = 0
            for x in nums:
                if _sum + x > target:
                    cnt += 1
                    _sum = x 
                else:
                    _sum += x 
            return cnt <= m 

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                # can be less
                hi = mid 
            else:
                # need to be larger
                lo = mid + 1
        return lo 
