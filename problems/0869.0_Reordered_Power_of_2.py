'''
Runtime: 4567 ms, faster than 12.83% of Python3 online submissions for Reordered Power of 2.
Memory Usage: 13.8 MB, less than 96.79% of Python3 online submissions for Reordered Power of 2.
'''
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = list(str(n))
        for p in permutations(digits):
            if p[0] == '0':
                continue
            x = int(''.join(p))
            if x > 0 and x & (x - 1) == 0:
                return True
        return False
        