'''
binary search
T: O(2 * N * log(max(*matrix) - min(*matrix)))
S: O(1)

Runtime: 272 ms, faster than 65.16% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.8 MB, less than 38.85% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lower, upper = matrix[0][0], matrix[-1][-1]
        ans = lower 
        
        def count_le(x):
            '''count less than or equal to x, sum of every row count'''
            cnt = 0
            i, j = 0, n - 1
            while i < n and j >= 0:
                if matrix[i][j] > x:
                    j -= 1
                else:
                    cnt += j + 1
                    i += 1
            return cnt 
        
        while lower <= upper:
            mid = (lower + upper) // 2 
            if count_le(mid) >= k:
                ans = mid 
                upper = mid - 1
            else:
                lower = mid + 1
        return ans 
