'''
Approach: Two Pointers
Time: O(n)
Space: O(n)

You are here!
Your runtime beats 43.37 % of python submissions.
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        leadingZero = trailingZero = canPlaceCount = 0
        size = len(flowerbed)
        i = 0
        while i < size:
            if flowerbed[i] == 0:
                leadingZero += 1
                i += 1
            else:
                break
        
        j = size - 1
        while j >= 0 and j > i:
            if flowerbed[j] == 0:
                trailingZero += 1
                j -= 1
            else:
                break
        
        midCount = 0
        if i < j:
            midZeros = ''.join([str(flower) for flower in flowerbed[i : j + 1]]).split('1')
            for mid in midZeros:
                if len(mid) >= 3:
                    midCount += (len(mid) - 1) / 2
                    
        if i == size:  # all zeros
            canPlaceCount += (leadingZero + 1) / 2
        else:
            canPlaceCount += leadingZero / 2
        canPlaceCount += trailingZero / 2
        canPlaceCount += midCount
        
        if canPlaceCount >= n:
            return True
        else:
            return False
        
'''
Input:
[0]
1
Output:
false
Expected:
true
'''


