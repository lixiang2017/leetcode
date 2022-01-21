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



