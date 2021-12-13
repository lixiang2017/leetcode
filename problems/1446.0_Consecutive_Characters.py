'''
Runtime: 44 ms, faster than 63.50% of Python3 online submissions for Consecutive Characters.
Memory Usage: 14.3 MB, less than 45.10% of Python3 online submissions for Consecutive Characters.
'''
class Solution:
    def maxPower(self, s: str) -> int:
        pre, power, max_power = None, 0, 0
        for ch in s:
            if pre == ch:
                power += 1
            else:
                pre = ch
                power = 1
            max_power = max(max_power, power)
        return max_power
        
        