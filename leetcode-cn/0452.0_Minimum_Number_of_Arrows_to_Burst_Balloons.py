'''
扫描线
sort

执行用时：252 ms, 在所有 Python3 提交中击败了42.07% 的用户
内存消耗：39.9 MB, 在所有 Python3 提交中击败了46.19% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort()
        last = points[0][1]
        for start, end in points:
            if start > last:
                ans += 1
                last = end
            if start < last:
                last = min(last, end)
        return ans + 1


'''
Runtime: 1824 ms, faster than 25.99% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
Memory Usage: 59.1 MB, less than 35.36% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort()
        last = points[0][1]
        for start, end in points:
            if start > last:
                ans += 1
                last = end
            if end < last:
                last = end
        return ans
            
            