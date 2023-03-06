'''
binary search

Runtime: 44 ms, faster than 96.22% of Python3 online submissions for Kth Missing Positive Number.
Memory Usage: 14.1 MB, less than 44.89% of Python3 online submissions for Kth Missing Positive Number.
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        missing = arr[-1] - len(arr)
        if k > missing:
            return arr[-1] + k - missing
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] - (mid + 1) >= k:
                r = mid - 1
            else:
                l = mid + 1     
        missing = arr[r + 1] - (r + 2)
        return arr[r + 1] - (missing - k) - 1

'''
binary search

Runtime: 54 ms, faster than 65.76% of Python3 online submissions for Kth Missing Positive Number.
Memory Usage: 14 MB, less than 44.89% of Python3 online submissions for Kth Missing Positive Number.
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        missing = arr[-1] - len(arr)
        if k > missing:
            return arr[-1] + k - missing
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] - (mid + 1) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return r + k + 1

'''
binary search

Runtime: 54 ms, faster than 65.76% of Python3 online submissions for Kth Missing Positive Number.
Memory Usage: 14 MB, less than 44.89% of Python3 online submissions for Kth Missing Positive Number.
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] - (mid + 1) >= k:
                r = mid - 1
            else:
                l = mid + 1     
        return r + k + 1

'''
执行用时：36 ms, 在所有 Python3 提交中击败了80.56% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了54.80% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        for i, x in enumerate(arr):
            if x - i - 1 >= k:
                return k + i 
        return k + n



'''
执行用时：40 ms, 在所有 Python3 提交中击败了59.48% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.15% 的用户
通过测试用例：84 / 84
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        return list(set(range(2001)) - set(arr))[k]
