class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), "b")


if __name__ == "__main__":
    a = "11"
    b = "1"
    assert Solution().addBinary(a, b) == "100"

    a = "1010"
    b = "1011"
    assert Solution().addBinary(a, b) == "10101"
