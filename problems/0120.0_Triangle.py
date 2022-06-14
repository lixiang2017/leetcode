'''
DP, modify nums in place
T: O(H^2)
S: O(1)

Runtime: 118 ms, faster than 26.08% of Python3 online submissions for Triangle.
Memory Usage: 14.9 MB, less than 60.15% of Python3 online submissions for Triangle.
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        t = triangle
        h = len(t)
        for i in range(h - 2, -1, -1):
            for j in range(i + 1):
                t[i][j] += min(t[i + 1][j], t[i + 1][j + 1])
        return t[0][0]
