'''
binary search
T: O(Nlog(max(piles)))
S: O(1)

执行用时：300 ms, 在所有 Python3 提交中击败了60.29% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了33.03% 的用户
通过测试用例：121 / 121
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =  1, max(piles)
        ans = r 

        def eat_all(c: int) -> bool:
            need = 0
            for p in piles:
                need += (p + c - 1) // c 
                if need > h:
                    return False 
            return True

        while l <= r:
            mid = l + (r - l) // 2
            if eat_all(mid):
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans 


'''
need += (p - 1) // c + 1 

执行用时：312 ms, 在所有 Python3 提交中击败了53.09% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了65.36% 的用户
通过测试用例：121 / 121
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =  1, max(piles)
        ans = r 

        def eat_all(c: int) -> bool:
            need = 0
            for p in piles:
                need += (p - 1) // c + 1 
                if need > h:
                    return False 
            return True

        while l <= r:
            mid = l + (r - l) // 2
            if eat_all(mid):
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans 


'''
return r + 1 

执行用时：300 ms, 在所有 Python3 提交中击败了60.29% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了18.31% 的用户
通过测试用例：121 / 121
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =  1, max(piles)

        def eat_all(c: int) -> bool:
            need = 0
            for p in piles:
                need += (p - 1) // c + 1 
                if need > h:
                    return False 
            return True

        while l <= r:
            mid = l + (r - l) // 2
            if eat_all(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1 


'''
执行用时：252 ms, 在所有 Python3 提交中击败了83.35% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了96.59% 的用户
通过测试用例：121 / 121
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =  1, max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            total = sum((p - 1) // mid + 1 for p in piles)
            if total <= h:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1






