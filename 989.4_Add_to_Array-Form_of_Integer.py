#! /usr/local/bin/python3
"""
Explanation
Take K as a carry.
Add it to the lowest digit,
Update carry K,
and Keep going to higher digit.

Time Complexity

Insert will take O(1) time or O(N) time on shifting, depending on the data stucture.
But in this problem K is at most 5 digit so this is restricted.
So this part doesn't matter.

The overall time complexity is O(N).
"""


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
        for i in range(len(A))[::-1]:
            A[i], K = (A[i] + K) % 10, (A[i] + K) / 10
        return [int(i) for i in str(K)] + A if K else A   


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
