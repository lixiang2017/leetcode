'''
approach: Greedy, from left to right
Time: O(2 * D) = O(D), where O(D) = O(logN) is the number of digits in N.
Space: O(D)

执行用时：24 ms, 在所有 Python 提交中击败了30.26%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了78.80%的用户
'''


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = map(int, str(N))
        L = len(digits)
        i = 0
        while i < L - 1 and digits[i] <= digits[i + 1]:
            i += 1
        if i == L - 1:
            return int(''.join(map(str, digits)))
    
        while i - 1 >= 0 and digits[i - 1] == digits[i]:
            i -= 1
        
        digits[i] -= 1
        digits[i + 1:] = [9] * (L - i - 1)
        return int(''.join(map(str, digits)))

'''
approach: Greedy, from right to left
Time: O(D ^ 2), where O(D) = O(logN) is the number of digits in N.
Space: O(D)

执行用时：12 ms, 在所有 Python 提交中击败了96.47%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了88.79%的用户
'''


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = map(int, str(N))
        L = len(digits)
        i = L - 1
        while i > 0:
            while i > 0 and digits[i - 1] <= digits[i]:
                i -= 1
            if i == 0:
                return int(''.join(map(str, digits)))            
            digits[i - 1] -= 1
            digits[i: ] = [9] * (L - i)
        return int(''.join(map(str, digits)))
