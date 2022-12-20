'''
binary search

执行用时：912 ms, 在所有 Python3 提交中击败了65.22% 的用户
内存消耗：24.1 MB, 在所有 Python3 提交中击败了33.82% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(m):
            op = 0
            for x in nums:
                op += (x - 1) // m
                if op > maxOperations:
                    return False 
            return True

        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1