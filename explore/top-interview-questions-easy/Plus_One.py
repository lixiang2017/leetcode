'''
You are here!
Your runtime beats 90.88 % of python submissions.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        reversed_digits = digits[:: -1]
        print 'reversed_digits: ', reversed_digits
        for i in range(len(reversed_digits)):
            if 0 == i:
                reversed_digits[i] = reversed_digits[i] + 1

            num = reversed_digits[i] + carry
            if 10 == num:
                reversed_digits[i] = 0
                carry = 1
            else:
                reversed_digits[i] = num
                carry = 0
                break

        # [9]
        if 1 == carry:
            reversed_digits.append(1)

        print reversed_digits[:: -1]
        return reversed_digits[:: -1]


if __name__ == '__main__':
    digits = [1,2,3]
    assert Solution().plusOne(digits) == [1,2,4]
    #Explanation: The array represents the integer 123.

    digits = [4,3,2,1]
    assert Solution().plusOne(digits) == [4,3,2,2]
    # Explanation: The array represents the integer 4321.

    digits = [0]
    assert Solution().plusOne(digits) == [1]

    digits = [5, 9, 9, 9]
    assert Solution().plusOne(digits) == [6, 0, 0, 0]

    digits = [4]
    assert Solution().plusOne(digits) == [5]


    digits = [9]
    assert Solution().plusOne(digits) == [1, 0]


