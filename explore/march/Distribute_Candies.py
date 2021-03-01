'''
approach: Set
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 92.11 % of python submissions.
You are here!
Your memory usage beats 79.93 % of python submissions.
'''


class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return min(len(set(candyType)), len(candyType) / 2)
