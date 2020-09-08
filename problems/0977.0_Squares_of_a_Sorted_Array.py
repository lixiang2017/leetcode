#! /usr/local/bin/python3

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i*i for i in A])

if __name__ == "__main__":
    A = [-4, -1, 0, 3, 10]
    assert Solution().sortedSquares(A) == [0, 1, 9, 16, 100]

    A = [-7, -3, 2, 3, 11]
    assert Solution().sortedSquares(A) == [4, 9, 9, 49, 121]
