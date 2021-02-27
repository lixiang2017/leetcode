class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(range(n + 1))



class Solution(object):
    def __init__(self):
        self.ans = 0
        
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        n > 1 and self.sumNums(n - 1)
        self.ans += n
        return self.ans


class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n and (n + self.sumNums(n - 1))


class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n + 1) * n / 2
    