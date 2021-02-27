'''
approach: Combination + Enumerate
Time: O(2 * N^2) = O(N^2)
Space: O(N^2)

执行用时：16 ms, 在所有 Python 提交中击败了79.07%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了75.58%的用户

ref:
https://leetcode-cn.com/problems/ccw6C7/solution/python3-zu-he-shu-mo-ban-mei-ju-by-yim-6-jf0r/
'''


class Solution(object):
    def paintingPlan(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k < 0 or k > n * n: return 0
        if k == n * n or k == 0: return 1
        # combinations
        C = [[1] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(i):
                C[i + 1][j + 1] = C[i][j] + C[i][j + 1]
        
        # enumerate
        plan = 0
        for i in range(n + 1):
            for j in range(n + 1):
                if i * n + j * n - i * j == k:
                    plan += C[n][i] * C[n][j]
        
        return plan




'''
        # print combinations
        for i in range(n + 1):
            print C[i]

n = 6
[1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1]
[1, 2, 1, 1, 1, 1, 1]
[1, 3, 3, 1, 1, 1, 1]
[1, 4, 6, 4, 1, 1, 1]
[1, 5, 10, 10, 5, 1, 1]
[1, 6, 15, 20, 15, 6, 1]

n = 10
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 4, 6, 4, 1, 1, 1, 1, 1, 1, 1]
[1, 5, 10, 10, 5, 1, 1, 1, 1, 1, 1]
[1, 6, 15, 20, 15, 6, 1, 1, 1, 1, 1]
[1, 7, 21, 35, 35, 21, 7, 1, 1, 1, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1, 1, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1, 1]
[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
'''