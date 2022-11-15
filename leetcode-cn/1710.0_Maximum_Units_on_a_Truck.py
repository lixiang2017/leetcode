'''
sort

执行用时：44 ms, 在所有 Python3 提交中击败了90.65% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了81.87% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda b: -b[1])
        ans = 0
        for n, units in boxTypes:
            if truckSize >= n:
                ans += n * units 
                truckSize -= n 
            else:
                ans += truckSize * units 
                break 
        return ans 
