'''
T: O(N^3)
S: O(N)

Runtime: 6107 ms, faster than 5.02% of Python3 online submissions for Max Points on a Line.
Memory Usage: 14 MB, less than 75.79% of Python3 online submissions for Max Points on a Line.
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # vertical line
        xc = Counter(x for x, y in points)
        ans = max(xc.values())
        
        # y = kx + b
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i != j and x1 != x2:
                    c = 2
                    for k, (x, y) in enumerate(points):
                        if k != i and k != j and (x2 - x1) * (y - y1) == (x - x1) * (y2 - y1):
                            c += 1
                    ans = max(ans, c)        
        
        return ans 

'''
不必单独讨论垂直情况
T: O(N^3)
S: O(1)

Runtime: 5913 ms, faster than 5.02% of Python3 online submissions for Max Points on a Line.
Memory Usage: 14 MB, less than 75.79% of Python3 online submissions for Max Points on a Line.
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        ans = 0
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i != j:
                    c = 2
                    for k, (x, y) in enumerate(points):
                        if k != i and k != j and (x2 - x1) * (y - y1) == (x - x1) * (y2 - y1):
                            c += 1
                    ans = max(ans, c)        
        return ans 

'''
if ans > n // 2 or ans > n - i:
    break
T: O(N^3)
S: O(1)  

Runtime: 968 ms, faster than 12.43% of Python3 online submissions for Max Points on a Line.
Memory Usage: 14 MB, less than 53.74% of Python3 online submissions for Max Points on a Line.
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        ans = 0
        n = len(points)
        for i, (x1, y1) in enumerate(points):
            if ans > n // 2 or ans > n - i:
                break
            for j in range(i + 1, n):
                x2, y2 = points[j]
                c = 2
                for k in range(j + 1, n):
                    x, y = points[k]
                    if (x2 - x1) * (y - y1) == (x - x1) * (y2 - y1):
                        c += 1
                ans = max(ans, c)        
        return ans 


'''
hash table

Runtime: 88 ms, faster than 88.58% of Python3 online submissions for Max Points on a Line.
Memory Usage: 13.9 MB, less than 75.79% of Python3 online submissions for Max Points on a Line.
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        ans = 0
        n = len(points)
        for i, (x1, y1) in enumerate(points):
            if ans > n // 2 or ans > n - i:
                break
            c = Counter()
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    if dy < 0:
                        dx = -dx 
                        dy = -dy
                    g = gcd(abs(dx), dy)
                    dx //= g
                    dy //= g
                c[(dx, dy)] += 1
             
            for slop, cnt in c.items():
                ans = max(ans, cnt + 1)        
        return ans 


'''
c[dx * 20001 + dy] += 1
hash table

Runtime: 84 ms, faster than 89.36% of Python3 online submissions for Max Points on a Line.
Memory Usage: 13.8 MB, less than 94.26% of Python3 online submissions for Max Points on a Line.
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        ans = 0
        n = len(points)
        for i, (x1, y1) in enumerate(points):
            if ans > n // 2 or ans > n - i:
                break
            c = Counter()
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    if dy < 0:
                        dx = -dx 
                        dy = -dy
                    g = gcd(abs(dx), dy)
                    dx //= g
                    dy //= g
                c[dx * 20001 + dy] += 1
             
            for slop, cnt in c.items():
                ans = max(ans, cnt + 1)        
        return ans 
