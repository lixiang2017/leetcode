class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda p: [p[0], -p[1]])
        ans, max_right = 0, -inf
        for a, b in intervals:
            if b > max_right:
                ans += 1
                max_right = b
        return ans
