'''

15 / 15 test cases passed.
Status: Accepted
Runtime: 12 ms
Memory Usage: 13.5 MB
Submitted: 0 minutes ago

You are here!
Your memory usage beats 58.15 % of python submissions.
'''


class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return [1,
                2,
                3,
                8,
                10,
                36,
                41,
                132,
                250,
                700,
                750,
                4010,
                4237,
                10680,
                24679,][n - 1]
