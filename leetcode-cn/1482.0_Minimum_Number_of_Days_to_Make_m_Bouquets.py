'''
approach: Sort + Binary Search
Time: O(NlogN + NlogN)
Space: O(N), for a list of a set

执行用时：1296 ms, 在所有 Python3 提交中击败了20.63%的用户
内存消耗：29.1 MB, 在所有 Python3 提交中击败了5.63%的用户
'''


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        days = sorted(set(bloomDay))
        N = len(bloomDay)
        def check(target):
            bouquet = 0
            i = adjacent = 0
            while i < N:
                if bloomDay[i] <= target:
                    adjacent += 1
                    if adjacent >= k:
                        bouquet += 1
                        adjacent = 0
                else:
                    adjacent = 0

                if bouquet >= m:
                    return True
                i += 1
            return False


        left, right = 0, len(days) - 1
        idx = 0
        while left <= right:
            mid = (right - left) // 2 + left
            if check(days[mid]):
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        return days[idx]


'''
approach: no Sort, just Binary Search
Time: O(NlogN)
Space: O(1)

执行用时：1988 ms, 在所有 Python3 提交中击败了5.00%的用户
内存消耗：25.6 MB, 在所有 Python3 提交中击败了20.00%的用户
'''
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        N = len(bloomDay)
        def check(target):
            bouquet = 0
            i = adjacent = 0
            while i < N:
                if bloomDay[i] <= target:
                    adjacent += 1
                    if adjacent >= k:
                        bouquet += 1
                        adjacent = 0
                else:
                    adjacent = 0

                if bouquet >= m:
                    return True
                i += 1
            return False

        left, right = 1, 10 ** 9
        ans = 0
        while left <= right:
            mid = (right - left) // 2 + left
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


