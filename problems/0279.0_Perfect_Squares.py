'''
BFS

Runtime: 623 ms, faster than 74.25% of Python3 online submissions for Perfect Squares.
Memory Usage: 30.6 MB, less than 12.10% of Python3 online submissions for Perfect Squares.
'''
class Solution:
    def numSquares(self, n: int) -> int:
        int(sqrt(n))
        squares = [i ** 2 for i in range(int(sqrt(n)), 0, -1)]
        step = 1
        q = [n - s for s in squares]
        while True:
            next_q = []
            for qq in q:
                if 0 == qq:
                    return step
                for s in squares:
                    if qq - s == 0:
                        return step + 1
                    elif qq > s:
                        next_q.append(qq - s)
                        
            q = next_q
            step += 1
