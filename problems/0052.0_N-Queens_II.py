'''
Runtime: 254 ms, faster than 9.76% of Python3 online submissions for N-Queens II.
Memory Usage: 13.9 MB, less than 39.44% of Python3 online submissions for N-Queens II.
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0
        q = [-1] * n 
        
        def backtrack(i):
            # i-th row
            nonlocal cnt
            if i == n:
                cnt += 1
                return
            # try every position for i-th row
            for j in range(n):
                # if not same column or diag
                if any(q[k] == j or abs(q[k] - j) == i - k for k in range(i)):
                    continue
                q[i] = j
                backtrack(i + 1)
                q[i] = -1
        
        backtrack(0)
        return cnt

'''
# q[i] = -1  # no use

Runtime: 260 ms, faster than 9.46% of Python3 online submissions for N-Queens II.
Memory Usage: 13.9 MB, less than 39.44% of Python3 online submissions for N-Queens II.
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        cnt = 0
        q = [-1] * n 
        
        def backtrack(i):
            # i-th row
            nonlocal cnt
            if i == n:
                cnt += 1
                return
            # try every position for i-th row
            for j in range(n):
                # if not same column or diag
                if any(q[k] == j or abs(q[k] - j) == i - k for k in range(i)):
                    continue
                q[i] = j
                backtrack(i + 1)
                # q[i] = -1  # no use
        
        backtrack(0)
        return cnt




'''
from  51. N-Queens

Runtime: 203 ms, faster than 12.73% of Python3 online submissions for N-Queens II.
Memory Usage: 14.2 MB, less than 5.13% of Python3 online submissions for N-Queens II.
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
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
        return len(ans)


