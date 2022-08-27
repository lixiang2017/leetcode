'''
binary search

Runtime: 2967 ms, faster than 79.05% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
Memory Usage: 14.7 MB, less than 92.49% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
'''
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float('-inf')
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                pre_sum = [0]
                s = 0
                for v in total:
                    s += v 
                    idx = bisect.bisect_left(pre_sum, s - k)
                    if idx != len(pre_sum):
                        ans = max(ans, s - pre_sum[idx])
                    bisect.insort(pre_sum, s)
        return ans 


'''
                    if s == k:
                        return k
                        
Runtime: 1778 ms, faster than 96.84% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
Memory Usage: 14.7 MB, less than 92.49% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
'''
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float('-inf')
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                pre_sum = [0]
                s = 0
                for v in total:
                    s += v 
                    if s == k:
                        return k
                    idx = bisect.bisect_left(pre_sum, s - k)
                    if idx != len(pre_sum):
                        ans = max(ans, s - pre_sum[idx])
                    bisect.insort(pre_sum, s)
        return ans 
    
