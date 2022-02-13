'''
hash table * 4, continue剪枝

执行用时：256 ms, 在所有 Python3 提交中击败了89.26% 的用户
内存消耗：30.7 MB, 在所有 Python3 提交中击败了36.13% 的用户
通过测试用例：45 / 45
'''
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = set()
        C = Counter
        row, col, diagonal, anti_diagonal = C(), C(), C(), C()
        for r, c in lamps:
            if (r, c) in points:
                continue
            points.add((r, c))
            row[r] += 1
            col[c] += 1
            diagonal[r - c] += 1
            anti_diagonal[r + c] += 1

        ans = []
        for r, c in queries:
            if row[r] or col[c] or diagonal[r - c] or anti_diagonal[r + c]:
                ans.append(1)
            else:
                ans.append(0)
                continue

            for nr in range(r - 1, r + 2):
                for nc in range(c - 1, c + 2):
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) in points:
                        points.remove((nr, nc))
                        row[nr] -= 1
                        col[nc] -= 1
                        diagonal[nr - nc] -= 1
                        anti_diagonal[nr + nc] -= 1

        return ans 
        
