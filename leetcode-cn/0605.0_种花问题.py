'''
Time: O(N)
Space: O(1)

执行结果：
通过
显示详情
执行用时：28 ms, 在所有 Python 提交中击败了96.85% 的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了72.30% 的用户
'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n: return True

        flowerbed = [0] + flowerbed + [0]
        size = len(flowerbed)
        for i in range(1, size - 1):
            if not (flowerbed[i - 1] or flowerbed[i] or flowerbed[i + 1]):
                flowerbed[i] = 1
                n -= 1
                if not n:
                    return True

        return False
