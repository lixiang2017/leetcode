class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        h = (hour + minutes / 60) / 12
        m = minutes / 60
        a = abs(h - m)
        a = min(a, 1.0 - a)
        return a * 360