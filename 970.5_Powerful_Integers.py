'''
Author: lixiang
Success
Details 
Runtime: 20 ms, faster than 83.61% of Python online submissions for Powerful Integers.
Memory Usage: 11.7 MB, less than 66.12% of Python online submissions for Powerful Integers.
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        # build a list of all x powers until bound
        xpow = []
        if x == 1:
            xpow = [1]
        else:
            _x = 1
            while _x < bound:
                xpow.append(_x)
                _x *= x
        # build a list of all y powers until bound   
        ypow = []
        if y == 1:
            ypow = [1]
        else:
            _y = 1
            while _y < bound:
                ypow.append(_y)
                _y *= y
        
        # get all relerant sums, now we only need to add. multiplication was done once
        # use set to remove duplicates
        ans = set([x + y for x in xpow for y in ypow if x + y <= bound])
        return list(ans)
        
if __name__ == "__main__":
    x = 2
    y = 3
    bound = 10
    assert Solution().powerfulIntegers(x, y, bound) == [2, 3, 4, 5, 7, 9, 10]

    x = 3
    y = 5
    bound = 15
    assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 6, 8, 10, 14]

    x = 1
    y = 1
    bound = 5
    assert Solution().powerfulIntegers(x, y, bound) == [2]

    x = 40
    y = 50
    bound = 10000
    print Solution().powerfulIntegers(x, y, bound) # [2, 41, 51, 90, 1601, 1650, 2501, 2540, 4100]
    # [1601, 2, 4100, 2501, 41, 2540, 1650, 51, 90]i

    x = 2
    y = 1
    bound = 10
    print Solution().powerfulIntegers(x, y, bound) # [9, 2, 3, 5] # The result is not sorted.
    # [2, 3, 5, 9]

    x = 1
    y = 3
    bound = 20
    assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 10]
