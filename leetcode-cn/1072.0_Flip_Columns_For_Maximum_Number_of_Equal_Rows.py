'''
执行用时：396 ms, 在所有 Python3 提交中击败了7.69% 的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了32.48% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern = []
        for row in matrix:
            pattern.append(''.join(map(str, row)))
            pattern.append(''.join(map(str, [1 - x for x in row])))
        return Counter(pattern).most_common(1)[0][1]


'''
执行用时：276 ms, 在所有 Python3 提交中击败了18.80% 的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了23.08% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern = []
        for row in matrix:
            pattern.append(''.join(map(str, row)))
            pattern.append(''.join(map(str, [1 - x for x in row])))
        return max(Counter(pattern).values())

'''
执行用时：216 ms, 在所有 Python3 提交中击败了27.35% 的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了40.17% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern = []
        for row in matrix:
            pattern.append(''.join(map(str, [x ^ row[0] for x in row])))
        return max(Counter(pattern).values())

'''
执行用时：240 ms, 在所有 Python3 提交中击败了21.37% 的用户
内存消耗：18.7 MB, 在所有 Python3 提交中击败了38.46% 的用户
通过测试用例：89 / 89
'''
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = Counter()
        for i in range(m):
            value = 0
            for j in range(n):
                value = value * 10 + (matrix[i][j] ^ matrix[i][0])
            count[value] += 1
        return max(count.values())
