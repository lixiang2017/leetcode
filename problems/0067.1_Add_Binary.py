class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = 0
        for i in a:
            int_a <<= 1
            int_a += int(i)

        int_b = 0
        for i in b:
            int_b <<= 1
            int_b += int(i)

        return format(int_a + int_b, "b")


if __name__ == "__main__":
    a = "11"
    b = "1"
    assert Solution().addBinary(a, b) == "100"

    a = "1010"
    b = "1011"
    assert Solution().addBinary(a, b) == "10101"
