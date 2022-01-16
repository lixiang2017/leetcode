'''
T: O(N)
S: O(1)

Runtime: 176 ms, faster than 32.33% of Python3 online submissions for Maximize Distance to Closest Person.
Memory Usage: 14.7 MB, less than 44.09% of Python3 online submissions for Maximize Distance to Closest Person.
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        i, j = 0, n - 1
        d1 = d2 = d3 = 0
        while i <= j and seats[i] == 0:
            i += 1
        d1 = i
        
        while i <= j and seats[j] == 0:
            j -= 1
        d3 = n - j - 1
        
        while i <= j:
            # skip 1
            while i <= j and seats[i] == 1:
                i += 1
            # count 0
            start = i
            while i <= j and seats[i] == 0:
                i += 1
            d2 = max(d2, (i - start + 1) // 2)
            
            i += 1    
        return max(d1, d2, d3)
