'''
ref:
https://leetcode-cn.com/problems/rectangle-area-ii/solution/ju-xing-mian-ji-ii-by-leetcode/

容斥原理

17 / 78 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 0 minutes ago
'''

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def intersect(rect1, rect2):
            return [
                max(rect1[0], rect2[0]),
                max(rect1[1], rect2[1]),
                min(rect1[2], rect2[2]),
                min(rect1[3], rect2[3]),                
            ]
        
        def area(rect):
            dx = max(0, rect[2] - rect[0])
            dy = max(0, rect[3] - rect[1])
            return dx * dy
        
        ans = 0
        for size in range(1, len(rectangles) + 1):
            for group in itertools.combinations(rectangles, size):
                ans += (-1) ** (size + 1) * area(reduce(intersect, group))
        
        return ans % (10 ** 9 + 7)



'''
压缩坐标

'''
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        N = len(rectangles)
        Xvals, Yvals = set(), set()
        for x1, y1, x2, y2 in rectangles:
            Xvals.add(x1); Xvals.add(x2)
            Yvals.add(y1); Yvals.add(y2)
        
        imapx = sorted(Xvals)
        imapy = sorted(Yvals)
        mapx = {x: i for i, x in enumerate(imapx)}
        mapy = {y: i for i, y in enumerate(imapy)}
        
        grid = [[0] * len(imapy) for _ in imapx]
        for x1, y1, x2, y2 in rectangles:
            for x in range(mapx[x1], mapx[x2]):
                for y in range(mapy[y1], mapy[y2]):
                    grid[x][y] = 1
        
        ans = 0
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val:
                    ans += (imapx[x+1] - imapx[x]) * (imapy[y+1] - imapy[y])
        
        return ans % (10**9 + 7)
