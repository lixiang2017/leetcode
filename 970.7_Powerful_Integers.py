# coding: UTF-8
'''
Author: lixiang
BFS Solution 
Start from helper(current value, x, y), we viewed each traversal as binary operations:
1. we multiple x by x, and add it to value to see if it is in bound 
2. we multiple y by y, and add it to value to see if it is in bound
3. if the above steps are in bound, we continue our BFS
Remember to use set/hashset to remove duplicate add operations.
Success
Details 
Runtime: 20 ms, faster than 83.61% of Python online submissions for Powerful Integers.
Memory Usage: 11.8 MB, less than 40.50% of Python online submissions for Powerful Integers.
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = set()

        def helper(last_num, left, right):
            value = left + right
            # print (left, right)
            if value <= bound:
                res.add(value)
                if x != 1:
                    helper(value, left * x, right)
                if y != 1:
                    helper(value, left, right * y)

        helper(0, 1, 1)
        return list(res)


if __name__ == "__main__":
    x = 2
    y = 3
    bound = 10
    # assert Solution().powerfulIntegers(x, y, bound) == [2, 3, 4, 5, 7, 9, 10]

    x = 3
    y = 5
    bound = 15
    # assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 6, 8, 10, 14]

    x = 1
    y = 1
    bound = 5
    # assert Solution().powerfulIntegers(x, y, bound) == [2]

    x = 40
    y = 50
    bound = 10000
    print Solution().powerfulIntegers(x, y, bound) # [2, 41, 51, 90, 1601, 1650, 2501, 2540, 4100]
    # [1601, 2, 4100, 2501, 41, 2540, 1650, 51, 90]i

    x = 2
    y = 1
    bound = 10
    # print Solution().powerfulIntegers(x, y, bound) # [9, 2, 3, 5] # The result is not sorted.
    # [2, 3, 5, 9]
 
    x = 1
    y = 3
    bound = 20
    # assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 10]

"""
# Pitfalls encountered during problem solving
"""
