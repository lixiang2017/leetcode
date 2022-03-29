'''
Runtime: 181 ms, faster than 33.70% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.2 MB, less than 55.07% of Python3 online submissions for The K Weakest Rows in a Matrix.
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        h = [(sum(row), i) for i, row in enumerate(mat)]
        # heapify(h)  # no need to heapify
        return [i for s, i in nsmallest(k, h)]


'''
Runtime: 197 ms, faster than 22.47% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.3 MB, less than 55.07% of Python3 online submissions for The K Weakest Rows in a Matrix.
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=lambda i: mat[i])[: k]

'''
Runtime: 116 ms, faster than 86.42% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.2 MB, less than 90.64% of Python3 online submissions for The K Weakest Rows in a Matrix.
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=lambda i: sum(mat[i]))[: k]
        

'''
Runtime: 217 ms, faster than 12.92% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 14.2 MB, less than 55.07% of Python3 online submissions for The K Weakest Rows in a Matrix.
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(range(len(mat)), key=mat.__getitem__)[: k]
