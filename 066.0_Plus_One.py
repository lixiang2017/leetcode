class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = "".join([str(i) for i in digits])
        n = int(s)
        n += 1
        digits = [int(i) for i in str(n)]
        return digits


if __name__ == "__main__":
    digits = [1, 2, 3]
    assert Solution().plusOne(digits) == [1, 2, 4]

    digits = [4, 3, 2, 1]
    assert Solution().plusOne(digits) == [4, 3, 2, 2]

    digits = [0]
    assert Solution().plusOne(digits) == [1]

    digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert Solution().plusOne(digits) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]

    digits = [9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert Solution().plusOne(digits) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]