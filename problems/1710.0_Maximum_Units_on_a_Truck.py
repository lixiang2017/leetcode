'''

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
    
    