'''
Binary Search

Runtime: 41 ms, faster than 41.71% of Python3 online submissions for Find in Mountain Array.
Memory Usage: 17 MB, less than 90.39% of Python3 online submissions for Find in Mountain Array.
'''
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        i, j = 0, n - 1
        # find peak index
        peak = i
        while i <= j:
            mid = (i + j) // 2
            if mid ==  0:
                mid += 1
            if mountain_arr.get(mid - 1) < mountain_arr.get(mid):
                peak = mid
                i = mid + 1
            else:
                j = mid - 1
                
        if mountain_arr.get(peak) == target:
            return peak
        
        # left part
        i, j = 0, peak
        while i <= j:
            mid = (i + j) // 2
            x = mountain_arr.get(mid)
            if x == target:
                return mid
            elif x < target:
                i = mid + 1
            else:
                j = mid - 1
        # right part
        i, j = peak + 1, n - 1
        while i <= j:
            mid = (i + j) // 2
            x = mountain_arr.get(mid)
            if x == target:
                return mid
            elif x < target:
                j = mid - 1
            else:
                i = mid + 1
                                    
        return -1

'''
[1,2,3,4,5,3,1]
3
[0,1,2,4,2,1]
3
[3,5,3,2,0]
0
'''


'''
Binary Search + Memoization

Runtime: 42 ms, faster than 33.95% of Python3 online submissions for Find in Mountain Array.
Memory Usage: 17.2 MB, less than 60.00% of Python3 online submissions for Find in Mountain Array.
'''
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # memo, index -> value
        memo = {}
        def get_value(index):
            if index in memo:
                return memo[index]
            memo[index] = mountain_arr.get(index)
            return memo[index]
            
        n = mountain_arr.length()
        i, j = 0, n - 1
        # find peak index
        peak = i
        while i <= j:
            mid = (i + j) // 2
            if mid ==  0:
                mid += 1
            
            if get_value(mid - 1) < get_value(mid):
                peak = mid
                i = mid + 1
            else:
                j = mid - 1
                
        if get_value(peak) == target:
            return peak
        
        # left part
        i, j = 0, peak
        while i <= j:
            mid = (i + j) // 2
            x = get_value(mid)
            if x == target:
                return mid
            elif x < target:
                i = mid + 1
            else:
                j = mid - 1
        # right part
        i, j = peak + 1, n - 1
        while i <= j:
            mid = (i + j) // 2
            x = get_value(mid)
            if x == target:
                return mid
            elif x < target:
                j = mid - 1
            else:
                i = mid + 1
                                    
        return -1





