'''
sort 
T: O(NlogN + N)
S: O(logN + 1)

Runtime: 158 ms, faster than 96.14% of Python3 online submissions for Maximum Units on a Truck.
Memory Usage: 14.4 MB, less than 83.07% of Python3 online submissions for Maximum Units on a Truck.
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda b: -b[1])
        ans = 0
        for box, unit in boxTypes:
            if box <= truckSize:
                ans += box * unit 
                truckSize -= box 
            else:
                ans += truckSize * unit 
                break 
        
        return ans 
    
