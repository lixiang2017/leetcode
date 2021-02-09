'''
approach: Hash Table
Time: O(highLimit - lowLimit)
Space: O(...)
'''


class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        seen = defaultdict(int)
        most = 0
        for num in range(lowLimit, highLimit + 1):
            digits_sum =  sum([int(d) for d in list(str(num))])
            seen[digits_sum] += 1
            if seen[digits_sum] > most:
                most = seen[digits_sum]
        return most
        