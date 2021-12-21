'''
执行用时：456 ms, 在所有 Python3 提交中击败了86.67% 的用户
内存消耗：35.1 MB, 在所有 Python3 提交中击败了26.67% 的用户
通过测试用例：119 / 119
'''
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        import math
        # math.degrees(math.pi)
        location_cnt = 0
        lx, ly = location
        degs = []
        for px, py in points:
            if px == lx and py == ly:
                location_cnt += 1
            else:
                deg = math.atan2(py - ly, px - lx)
                degs.append(deg)
        degs.sort()
        degs += [deg + 2 * pi for deg in degs]

        maxm, i, j, n = 0, 0, 0, len(degs) // 2
        d = angle / 180 * pi 
        while i < n and j < 2 * n:
            while j < 2 * n and degs[i] + d >= degs[j]:
                j += 1
            maxm = max(maxm, j - i)
            i += 1

        return maxm + location_cnt
        