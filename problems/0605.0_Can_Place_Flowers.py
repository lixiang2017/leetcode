'''
Runtime: 205 ms, faster than 33.05% of Python3 online submissions for Can Place Flowers.
Memory Usage: 14.6 MB, less than 31.20% of Python3 online submissions for Can Place Flowers.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 1:
                continue

            if size == 1 or (i == 0 and flowerbed[i + 1] == 0) \
                or (i == size - 1 and flowerbed[i - 1] == 0 ) \
                or (i > 0 and i < size and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                
            if n <= 0:
                return True
        
        return n <= 0

'''
[1]
0
[0,0,0,0,0,1,0,0]
0
'''



'''
Runtime: 247 ms, faster than 22.31% of Python3 online submissions for Can Place Flowers.
Memory Usage: 14.5 MB, less than 84.06% of Python3 online submissions for Can Place Flowers.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if 0 == n:
            return True
        
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 1:
                continue

            if size == 1 or (i == 0 and flowerbed[i + 1] == 0) \
                or (i == size - 1 and flowerbed[i - 1] == 0 ) \
                or (i > 0 and i < size and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                
            if n == 0:
                return True
        
        return False



'''
Runtime: 170 ms, faster than 55.56% of Python3 online submissions for Can Place Flowers.
Memory Usage: 14.4 MB, less than 65.78% of Python3 online submissions for Can Place Flowers.
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return flowerbed[0] + n < 2
        # two ends
        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if len(flowerbed) > 1 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1        
        if n <= 0:
            return True
        
        # middle
        i, m = 1, len(flowerbed)
        while i < m - 1:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                if 0 == n:
                    return True
                i += 2
            else:
                i += 1
        return False
        
'''
Input
[0,0,1,0,1]
1
Output
false
Expected
true


Input: [0]
1
Output: false
Expected: true
'''
