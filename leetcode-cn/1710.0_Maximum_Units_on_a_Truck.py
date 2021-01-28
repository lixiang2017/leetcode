'''
approach: Greedy + Sort
Time: O(NlogN + N) = O(NlogN)
Space: O(1)

Hints:
1. If we have space for at least one box, it's always optimal to put the box with the most units.
2. Sort the box with the number of units per box non-increasingly.
3. Iterate on the box types and take from each type as many as you can.

执行结果：
通过
显示详情
执行用时：32 ms, 在所有 Python 提交中击败了94.44%的用户
内存消耗：
13.5 MB, 在所有 Python 提交中击败了41.67%的用户
'''

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        total_units = 0
        for box, unit in boxTypes:
            if truckSize >= box:
                total_units += box * unit
                truckSize -= box
            elif truckSize > 0:
                total_units += truckSize * unit
                break
        
        return total_units
