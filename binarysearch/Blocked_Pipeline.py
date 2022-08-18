'''
Question 1018 of 1037

two types of blocking pair
1. vertical pair
     |
     |
2. slop pair
    \
     \ 
    or 
     /
    /
 

ref:
https://hackerranksolution.in/blockedpipelinegoogle/

Your code took 176 milliseconds — faster than 56.00% in Python
'''
class Solution:
    def solve(self, n, requests):
        m = [[0] * n for _ in range(2)]
        ans = 0
        # blocked pairs
        pair = set()
        for r, c, t in requests:
            for nc in (c - 1, c, c + 1):
                if 0 <= nc < n:
                    if t == 1:
                        if 1 == m[1 - r][nc]:
                            pair.add((r, c, 1 - r, nc))
                            # pair.add((1 - r, nc, r, c))                        
                    else:
                        if 1 == m[1 - r][nc]:
                            pair.discard((r, c, 1 - r, nc))
                            pair.discard((1 - r, nc, r, c))
            m[r][c] = t
            if not pair and (not (m[0][-1] & m[1][-1])):
                ans += 1
        return ans        


'''
Your code took 133 milliseconds — faster than 80.00% in Python
'''
class Solution:
    def solve(self, n, requests):
        m = [[0] * n for _ in range(2)]
        ans = 0
        # blocked pairs
        vertical = slop = 0
        for r, c, t in requests:
            for nc in (c - 1, c + 1):
                if 0 <= nc < n:
                    if t == 1:
                        if 1 == m[1 - r][nc] and 0 == m[r][c]:
                            slop += 1                   
                    else:
                        if 1 == m[1 - r][nc] and 1 == m[r][c]:
                            slop -= 1
            if t == 0:
                if 1 == m[1 - r][c] and 1 == m[r][c]:
                    vertical -= 1
            else:
                if 1 == m[1 - r][c] and 0 == m[r][c]:
                    vertical += 1
            m[r][c] = t
            if 0 == vertical and 0 == slop:
                ans += 1
        return ans  

'''
n = 4
requests = [
    [1, 2, 1],
    [0, 1, 0]
]


n = 4
requests = [
    [1, 2, 1],
    [0, 1, 0]
]
'''
