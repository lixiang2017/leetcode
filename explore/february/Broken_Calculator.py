'''
approach: Greedy + Recursion
Time: O(logY) -> O(log(Y/X)), because every two iteration number decreased at least twice.
Space: O(logY) -> O(log(Y/X)), because we use recursion. It can be made O(1) if we do it iteratively.

Thinking reversely

ref:
https://leetcode.com/problems/broken-calculator/discuss/1076046/Python-Greedy-solution-explained
https://leetcode.com/problems/broken-calculator/discuss/234484/JavaC%2B%2BPython-Change-Y-to-X-in-1-Line


You are here!
Your runtime beats 98.33 % of python submissions.
You are here!
Your memory usage beats 66.67 % of python submissions.
'''


class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X >= Y:
            # print '1X: ', X, 'Y: ', Y
            return X - Y
        
        if Y & 1 == 0:   # if Y % 2 == 0:
            # print '2X: ', X, 'Y: ', Y
            return 1 + self.brokenCalc(X, Y / 2)
        else:
            # print '3X: ', X, 'Y: ', Y
            return 1 + self.brokenCalc(X, Y + 1)
        
'''
1
1000000000

Your input
1
1000000000
Your stdout
2X:  1 Y:  1000000000
2X:  1 Y:  500000000
2X:  1 Y:  250000000
2X:  1 Y:  125000000
2X:  1 Y:  62500000
2X:  1 Y:  31250000
2X:  1 Y:  15625000
2X:  1 Y:  7812500
2X:  1 Y:  3906250
3X:  1 Y:  1953125
2X:  1 Y:  1953126
3X:  1 Y:  976563
2X:  1 Y:  976564
2X:  1 Y:  488282
3X:  1 Y:  244141
2X:  1 Y:  244142
3X:  1 Y:  122071
2X:  1 Y:  122072
2X:  1 Y:  61036
2X:  1 Y:  30518
3X:  1 Y:  15259
2X:  1 Y:  15260
2X:  1 Y:  7630
3X:  1 Y:  3815
2X:  1 Y:  3816
2X:  1 Y:  1908
2X:  1 Y:  954
3X:  1 Y:  477
2X:  1 Y:  478
3X:  1 Y:  239
2X:  1 Y:  240
2X:  1 Y:  120
2X:  1 Y:  60
2X:  1 Y:  30
3X:  1 Y:  15
2X:  1 Y:  16
2X:  1 Y:  8
2X:  1 Y:  4
2X:  1 Y:  2
1X:  1 Y:  1

Your answer
39
Expected answer
39
'''





'''
first attempt failed
Submission Result: Wrong Answer
'''

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X >= Y:
            return X - Y
        
        # X < Y
        operations = 0
        while Y & 1 == 0:
            Y >>= 1
            operations += 1
            if X >= Y:
                return operations + X - Y
        # still X < Y
        while X < Y:
            X <<= 1
            operations += 1
        
        return operations + X - Y

'''
Input:
1
1000000000
Output:
144057
Expected:
39
'''





'''
approach: Work Backwards (Greedy + Iteration)
Time: O(logY) -> O(log(Y/X))
Space: O(1)

ref:
https://leetcode.com/problems/broken-calculator/solution/

Success
Details 
Runtime: 16 ms, faster than 73.33% of Python online submissions for Broken Calculator.
Memory Usage: 13.4 MB, less than 40.00% of Python online submissions for Broken Calculator.
'''


class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        operations = 0
        while X < Y:
            operations += 1
            if Y & 1:
                Y += 1
            else:
                Y >>= 1
        
        return operations + X - Y
    
'''
You are here!
Your runtime beats 73.33 % of python submissions.
You are here!
Your memory usage beats 23.33 % of python submissions.
'''

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        operations = 0
        while X < Y:
            operations += Y % 2 + 1
            Y = (Y + 1) / 2
        
        return operations + X - Y


'''
approach: 1 line Recursive Solution
ref:
https://leetcode.com/problems/broken-calculator/discuss/234484/JavaC%2B%2BPython-Change-Y-to-X-in-1-Line

You are here!
Your runtime beats 53.33 % of python submissions.
You are here!
Your memory usage beats 66.67 % of python submissions.
'''

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        return X - Y if X >= Y else 1 + self.brokenCalc(X, Y + 1 if Y & 1 else Y / 2)




