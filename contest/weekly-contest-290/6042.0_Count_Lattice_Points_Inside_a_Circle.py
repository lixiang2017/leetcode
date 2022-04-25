'''
执行用时：1052 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：19.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        seen = set()
        for x, y, r in circles:
            for xx in range(x - r, x + r + 1):
                dy2 = r * r - (x - xx) ** 2
                dy = int(sqrt(dy2))
                for yy in range(y - dy, y + dy + 1):
                    seen.add((xx, yy))

        return len(seen)


'''
执行用时：4928 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        for x in range(201):
            for y in range(201):
                inside = False 
                for x0, y0, r in circles:
                    if (x - x0) * (x - x0) + (y - y0) * (y - y0) <= r * r:
                        inside = True
                        break 
                if inside:
                    ans += 1
        return ans 


'''
执行用时：4884 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        for x in range(201):
            for y in range(201):
                for x0, y0, r in circles:
                    if (x - x0) * (x - x0) + (y - y0) * (y - y0) <= r * r:
                        ans += 1
                        break 
        return ans 


'''
执行用时：812 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        # sort circles by radius desc
        circles.sort(key = lambda c: -c[2])
        minx = maxx = circles[0][0]
        miny = maxy = circles[0][1]
        for x, y, r in circles:
            minx = min(minx, x - r)
            maxx = max(maxx, x + r)
            miny = min(miny, y - r)
            maxy = max(maxy, y + r)

        for i in range(minx, maxx + 1):
            for j in range(miny, maxy + 1):
                for x, y, r in circles:
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                        ans += 1
                        break 
        return ans 



'''
执行用时：992 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        # sort circles by radius desc
        circles.sort(key = lambda c: -c[2])
        maxx = circles[0][0]
        maxy = circles[0][1]
        for x, y, r in circles:
            maxx = max(maxx, x + r)
            maxy = max(maxy, y + r)

        for i in range(maxx + 1):
            for j in range(maxy + 1):
                for x, y, r in circles:
                    if (i - x) * (i - x) + (j - y) * (j - y) <= r * r:
                        ans += 1
                        break 
        return ans 


'''
执行用时：1008 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        # sort circles by radius desc
        circles.sort(key = lambda c: -c[2])
        minx = maxx = circles[0][0]
        miny = maxy = circles[0][1]
        for x, y, r in circles:
            minx = min(minx, x - r)
            maxx = max(maxx, x + r)
            miny = min(miny, y - r)
            maxy = max(maxy, y + r)

        for i in range(minx, maxx + 1):
            for j in range(miny, maxy + 1):
                ans += any((i - x) * (i - x) + (j - y) * (j - y) <= r * r for x, y, r in circles)
        return ans 


'''
二维差分数组
T: O(N^2)
S: O(N^2)

执行用时：68 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        maxx = max(x + r for x, y, r in circles) + 2
        maxy = max(y + r for x, y, r in circles) + 1
        diffs = [[0] * maxx for _ in range(maxy)]
        for x, y, r in circles:
            for yy in range(y - r, y + r + 1):
                z = isqrt(r * r - (y - yy) * (y - yy))
                diffs[yy][x - z] += 1
                diffs[yy][x + z + 1] -= 1
        return sum(sum(cur > 0 for cur in  accumulate(xs)) for xs in diffs)




'''
二维差分数组, 另一种写法

执行用时：100 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        maxx = maxy = 0
        for x, y, r in circles:
            maxx = max(maxx, x + r)
            maxy = max(maxy, y + r)
            
        diffs = [[0] * (maxx + 2) for _ in range(maxy + 1)]
        for x, y, r in circles:
            # [x1, x2]    # [left, right]
            x1 = x2 = x 
            # upper half
            for yy in range(y + r, y - 1, -1):
                while (x - x1) * (x - x1) + (y - yy) * (y - yy) <= r * r: x1 -= 1
                while (x - x2) * (x - x2) + (y - yy) * (y - yy) <= r * r: x2 += 1
                diffs[yy][x1 + 1] += 1
                diffs[yy][x2] -= 1
            # lower half
            x1 = x2 = x
            for yy in range(y - r, y):
                while (x - x1) * (x - x1) + (y - yy) * (y - yy) <= r * r: x1 -= 1
                while (x - x2) * (x - x2) + (y - yy) * (y - yy) <= r * r: x2 += 1
                diffs[yy][x1 + 1] += 1
                diffs[yy][x2] -= 1

        ans = 0
        for y in range(maxy + 1):
            cur = 0
            for x in range(maxx + 2):
                cur += diffs[y][x]
                if cur:
                    ans += 1
        return ans 


'''
二维差分数组, 只需要计算1/4圆即可。
重复累加没有关系，最终只是判断是否覆盖。
所以多加几次都没有关系，并不影响答案的正确性。 其实里面只有中间的一条最长直径是多算了。

执行用时：76 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        maxx = maxy = 0
        for x, y, r in circles:
            maxx = max(maxx, x + r)
            maxy = max(maxy, y + r)
            
        diffs = [[0] * (maxx + 2) for _ in range(maxy + 1)]
        for x, y, r in circles:
            # [x1, x2]    # [left, right]  x1 = x2 = x 
            step = 0
            for dy in range(r, -1, -1):
                while step * step + dy * dy <= r * r: step += 1
                # upper half
                diffs[y + dy][x - step + 1] += 1
                diffs[y + dy][x + step]     -= 1
                # lower half
                if dy != 0:
                    diffs[y - dy][x - step + 1] += 1
                    diffs[y - dy][x + step]     -= 1

        ans = 0
        for y in range(maxy + 1):
            cur = 0
            for x in range(maxx + 2):
                cur += diffs[y][x]
                if cur:
                    ans += 1
        return ans 



'''
no need to use  if dy != 0:

执行用时：72 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：60 / 60
'''
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        minx = maxx = circles[0][0]
        miny = maxy = circles[0][1]
        for x, y, r in circles:
            minx = min(minx, x - r)
            maxx = max(maxx, x + r)
            miny = min(miny, y - r)
            maxy = max(maxy, y + r)

        diffs = [[0] * (maxx + 2) for _ in range(maxy + 1)]
        for x, y, r in circles:
            step = 0
            for dy in range(r, -1, -1):
                while step * step + dy * dy <= r * r: step += 1
                # upper half
                diffs[y + dy][x - step + 1] += 1
                diffs[y + dy][x + step]     -= 1
                # lower half
                diffs[y - dy][x - step + 1] += 1
                diffs[y - dy][x + step]     -= 1

        ans = 0
        for y in range(miny, maxy + 1):
            cur = 0
            for x in range(minx, maxx + 2):
                cur += diffs[y][x]
                if cur:
                    ans += 1
        return ans 





