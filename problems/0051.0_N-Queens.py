'''
Runtime: 209 ms, faster than 14.27% of Python3 online submissions for N-Queens.
Memory Usage: 14.5 MB, less than 45.52% of Python3 online submissions for N-Queens.
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        # queens index
        q = [-1] * n 

        def backtrack(i):
            '''i-th row
            '''
            if i == n:
                ans.append(['.' * idx + 'Q' + '.' * (n - idx - 1) for idx in q])
                return 
            # try every position on i-th row 
            for j in range(n):
                if any(abs(q[k] - j) == i - k or q[k] == j for k in range(i)):
                    continue
                q[i] = j
                backtrack(i + 1)
                q[i] = -1

        backtrack(0)
        return ans




