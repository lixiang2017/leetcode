'''
268ms 击败 84.68%使用 Python3 的用户
20.08MB 击败 34.68%使用 Python3 的用户
'''
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        total = len(ranks)
        n = (cars + total - 1) // total 

        def check(m):
            return sum(isqrt(m // r) for r in ranks) >= cars
                
        low, high = 0, max(ranks) * n * n
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return high + 1
