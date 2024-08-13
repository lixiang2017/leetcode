'''
bitmask + itertools.combinations
'''
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        nums = []
        for row in matrix:
            b = 0
            for j, x in enumerate(row):
                b |= (x << j)
            nums.append(b)

        for cols in itertools.combinations(range(n), numSelect):
            b = 0
            for c in cols:
                b |= (1 << c)
            covered = 0
            for x in nums:
                if b & x == x:
                    covered += 1
            ans = max(ans, covered)
        return ans
