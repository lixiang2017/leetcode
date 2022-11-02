'''
leetcode.cn 前端界面更新了

不一定在给出的这些点里取得最大值，所以要遍历所有点。

时间876 ms
击败
81.25%
内存15.1 MB
击败
39.6%
'''
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        mx = my = maxq = 0
        for x in range(51):
            for y in range(51):
                total = 0
                for x1, y1, q1 in towers:
                    d2 = (x - x1) * (x - x1) + (y - y1) * (y - y1)
                    if d2 <= radius * radius:
                        total += q1 // (1 + sqrt(d2))
                if total > maxq or (total == maxq and (x < mx or (x == mx and y < my))):
                    maxq = total
                    mx = x 
                    my = y
        return [mx, my]
