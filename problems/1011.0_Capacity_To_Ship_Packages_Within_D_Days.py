'''
binary search

Runtime: 533 ms, faster than 54.81% of Python3 online submissions for Capacity To Ship Packages Within D Days.
Memory Usage: 17.1 MB, less than 31.63% of Python3 online submissions for Capacity To Ship Packages Within D Days.
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        def reachable(capacity):
            d, cur_w = 1, 0
            for w in weights:
                cur_w += w
                if cur_w > capacity:
                    d += 1
                    cur_w = w
                if d > days:
                    return False
            return True
        
        while l <= r:
            mid = (l + r) // 2
            if reachable(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1
