#! /usr/local/bin/python3

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A_str = ''.join([n for n in str(A) if n.isdigit()])
        A_int = int(A_str)
        sum = A_int + K
        return [int(c) for c in str(sum)]


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
