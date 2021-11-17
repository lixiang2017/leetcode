'''
执行用时：40 ms, 在所有 Python3 提交中击败了82.45% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了42.55% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(chain(*matrix))[k - 1]

'''
执行用时：60 ms, 在所有 Python3 提交中击败了46.46% 的用户
内存消耗：17.7 MB, 在所有 Python3 提交中击败了31.48% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(sum(matrix, []))[k - 1]

'''
执行用时：120 ms, 在所有 Python3 提交中击败了7.76% 的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了5.05% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return heapq.nsmallest(k, sum(matrix, []))[-1]


'''
binary search
T: O(10^9 * NlogN)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了58.06% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了52.86% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi, kth = matrix[0][0], matrix[-1][-1], 0

        def enough(val):
            cnt = 0
            for row in range(n):
                l, r = 0, n - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[row][mid] <= val:
                        l = mid + 1
                    else:
                        r = mid - 1
                cnt += l
            return cnt >= k

        while lo <= hi:
            mid = (lo + hi) // 2
            if enough(mid):
                kth = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return kth


'''
heapq

执行用时：112 ms, 在所有 Python3 提交中击败了8.81% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了63.55% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # (val, i, j)
        h = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(h)

        for _ in range(k):
            val, i, j = heapq.heappop(h)
            if j + 1 < n:
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
        return val


'''
T:O(2N*log(r-l)),S:O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了82.45% 的用户
内存消耗：17.5 MB, 在所有 Python3 提交中击败了49.10% 的用户
通过测试用例：86 / 86
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r, kth = matrix[0][0], matrix[-1][-1], 0

        def enough(val):
            cnt = 0
            i, j = 0, n - 1
            while i < n and j >= 0:
                if matrix[i][j] <= val:
                    cnt += j + 1
                    i += 1
                else:
                    j -= 1
            return cnt >= k
        
        while l <= r:
            mid = (l + r) // 2
            if enough(mid):
                kth = mid 
                r = mid - 1
            else:
                l = mid + 1

        return kth 


