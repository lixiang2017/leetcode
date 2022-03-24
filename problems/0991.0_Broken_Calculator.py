'''
逆向思维
DFS

Runtime: 28 ms, faster than 94.52% of Python3 online submissions for Broken Calculator.
Memory Usage: 13.9 MB, less than 73.06% of Python3 online submissions for Broken Calculator.
'''
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target:
            return startValue - target
        if target & 1:
            return 1 + self.brokenCalc(startValue, target + 1)
        else:
            return 1 + self.brokenCalc(startValue, target // 2)
        
