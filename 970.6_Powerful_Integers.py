# coding: UTF-8
'''
Author: lixiang
BFS 
NameError: global name 'bound' is not defined
'''

class Solution(object):
    def __init__(self):
        self.res = set()

    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        self.res = set()
        self.helper(0, 1, 1)
        return list(self.res)
        

    def helper(self, last_num, left, right):
        value = left + right
        # print (left, right)
        if value <= bound:
            self.res.add(value)
            if x != 1:
                self.helper(value, left * x, right)
            if y != 1:
                self.helper(value, left, right * y)



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

"""
# Pitfalls encountered during problem solving
## RuntimeError: maximum recursion depth exceeded while getting the repr of an object
两个if应该放在if value <= bound:里面
## SyntaxError: Non-ASCII character '\xe4' in file 970.6_Powerful_Integers.py on line 71,
## but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
put #coding: UTF-8 in the first line.
"""
