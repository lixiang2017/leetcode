'''
52 / 52 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 15.3 MB
提交时间：1 天前
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for _, i in sorted([(sum(row), i)  for i, row in enumerate(mat)])[: k]]




'''
执行用时：40 ms, 在所有 Python3 提交中击败了51.87% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了93.69% 的用户
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted([i for i in range(len(mat))], key=lambda i: sum(mat[i]))[: k]

'''
SyntaxError: Generator expression must be parenthesized
                  ^
    return sorted(i for i in range(len(mat)), key = lambda i: sum(mat[i]))[: k]
Line 3  (Solution.py)
'''


'''
heapq

执行用时：32 ms, 在所有 Python3 提交中击败了87.38% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了60.16% 的用户
'''
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pos_idx = []
        M, N = len(mat), len(mat[0])
        for i in range(M):
            l, r = 0, N - 1
            pos = -1
            while l <= r:
                mid = (l + r) // 2
                if mat[i][mid] == 0:
                    r = mid - 1
                else:
                    pos = mid
                    l = mid + 1
            pos_idx.append((pos + 1, i))
        
        heapq.heapify(pos_idx)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(pos_idx)[1])
        return ans

