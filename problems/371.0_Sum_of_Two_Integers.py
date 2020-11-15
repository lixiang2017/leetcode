'''
You are here!
Your runtime beats 38.63 % of python submissions.
'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # return a + b  # ok
        # return sum([a, b])  # ok
        return operator.add(a, b)  # ok
        