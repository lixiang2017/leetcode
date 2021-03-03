'''
approach: Dynamic Programming
Time: O(N)
Space: O(N)
'''


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0] * (num + 1)
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits[i] = bits[i - highBit] + 1
        return bits

'''
approach: Brute Force
'''

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def countOnes(x):
            ones = 0
            while x > 0:
                x &= (x - 1)
                ones += 1
            return ones
        return [countOnes(i) for i in range(num + 1)]

'''
approach: Dynamic Programming
Time: O(N)
Space: O(N)
'''       

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits

'''
approach: Dynamic Programming + lowbit
Time: O(N)
Space: O(N)
'''       


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0]
        for i in range(1, num + 1):
            # bits.append(bits[i >> 1] + (i & 1))
            bits.append(bits[i & (i - 1)] + 1)
        return bits



