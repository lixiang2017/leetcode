#! /usr/local/bin/python3


class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        ""[summary]
        Returns:
            [type] -- [description]
        """
        Klist = [int(i) for i in str(K)]
        carry = 0
        ans = []

        from itertools import izip_longest
        for i, j in izip_longest(A[::-1], Klist[::-1], fillvalue = 0):
            ans.append( (i + j + carry) % 10)
            carry = (i + j + carry) // 10
        if carry == 1:
            ans.append(1)

        return ans[::-1]


if __name__ == '__main__':
    A = [1, 2, 0, 0]
    K = 34
    assert Solution().addToArrayForm(A, K) == [1, 2, 3, 4]

    A = [2, 7, 4]
    K = 181
    assert Solution().addToArrayForm(A, K) == [4, 5, 5]

    A = [2, 1, 5]
    K = 806
    assert Solution().addToArrayForm(A, K) == [1, 0, 2, 1]

    A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    K = 1
    assert Solution().addToArrayForm(A, K) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
