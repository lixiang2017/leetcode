'''
Runtime: 51 ms, faster than 54.67% of Python3 online submissions for Find the Highest Altitude.
Memory Usage: 16.3 MB, less than 26.06% of Python3 online submissions for Find the Highest Altitude.
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = altitude = 0
        for g in gain:
            altitude += g
            ans = max(ans, altitude)
        return ans

'''
Runtime: 57 ms, faster than 16.50% of Python3 online submissions for Find the Highest Altitude.
Memory Usage: 16.1 MB, less than 91.15% of Python3 online submissions for Find the Highest Altitude.
'''
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))
        