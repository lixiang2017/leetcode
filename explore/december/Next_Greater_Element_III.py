'''

You are here!
Your runtime beats 100.00 % of python submissions.
'''

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(map(int, str(n)))
        size = len(digits)
        if 1 == size: return -1
        idx = size - 1
        while idx - 1 >= 0 and digits[idx] <= digits[idx - 1]:
            idx -= 1
        
        if idx == 0: return -1
        j = idx
        while j <= size - 1 and digits[j] > digits[idx - 1]:
            j += 1
            
        digits[idx - 1], digits[j - 1] = digits[j - 1], digits[idx - 1]
        digits[idx: ] = reversed(digits[idx: ])
        
        greater = int(''.join(map(str, digits)))
        return greater if greater <= (1 << 31 - 1) else -1
    