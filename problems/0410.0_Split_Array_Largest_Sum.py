'''
binary search

Runtime: 69 ms, faster than 37.69% of Python3 online submissions for Split Array Largest Sum.
Memory Usage: 14 MB, less than 37.77% of Python3 online submissions for Split Array Largest Sum.
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def check(s):
            # count group, current sum
            cnt, cur_s = 1, 0
            for x in nums:
                if cur_s + x > s:
                    cnt += 1
                    cur_s = x
                else:
                    cur_s += x
            return cnt <= m
        
        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1
            
