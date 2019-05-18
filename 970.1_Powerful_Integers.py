'''
Author: lixiang
Success
Runtime: 12 ms, faster than 99.63% of Python online submissions for Powerful Integers.
Memory Usage: 11.7 MB, less than 82.64% of Python online submissions for Powerful Integers.
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """

        import math
        b = bound

        if x != 1:
            b1 = int(math.log(bound, x)) + 1
        else:
            b1 = 1  # set range to 1

        if y != 1:
            b2 = int(math.log(bound, y)) + 1
        else:
            b2 = 1  # set range to 1

        ans = []
        for p in range(b1):
            for  q in range(b2):
                sum = x ** p + y ** q

                if sum <= bound:
                    ans.append(sum)
                else:   # sum > bound
                    break 

        ans = sorted(list(set(ans)))
        return ans
        
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
    Solution().powerfulIntegers(x, y, bound) == [2, 41, 51, 90, 1601, 1650, 2501, 2540, 4100]

    x = 2
    y = 1
    bound = 10
    assert Solution().powerfulIntegers(x, y, bound) == [2, 3, 5, 9]

    x = 1
    y = 3
    bound = 20
    assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 10]


'''
# Pitfalls encoutered during problem solving
## Runtime Error Message: Line 13: ZeroDivisionError: float division by zero
the base in function math.log(x[, base]) can not be 1!
'''

