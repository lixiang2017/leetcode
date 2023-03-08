'''
binary search
T: O(NlogN)
S: O(1)

Runtime: 748 ms, faster than 22.43% of Python3 online submissions for Koko Eating Bananas.
Memory Usage: 15.6 MB, less than 60.66% of Python3 online submissions for Koko Eating Bananas.
'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minp, maxp = min(piles), max(piles)
        ans = maxp
        l, r = 1, maxp
        while l <= r:    
            mid = (l + r) // 2
            need = 0
            for p in piles:
                q, rem = divmod(p, mid)
                need += q
                if rem != 0:
                    need += 1
                if need > h:
                    l = mid + 1
                    break
            if need <= h:
                ans = mid
                r = mid - 1
        return ans

'''
Input: [312884470]
312884469
Output: 312884470
Expected: 2    
'''



'''
Runtime: 467 ms, faster than 75.88% of Python3 online submissions for Koko Eating Bananas.
Memory Usage: 15.6 MB, less than 16.17% of Python3 online submissions for Koko Eating Bananas.
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        def canFinish(k):
            t = 0
            for p in piles:
                t += (p + k - 1) // k
                if t > h:
                    return False
            return True
        
        while l <= r:
            mid = (l + r) // 2
            if canFinish(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1

        