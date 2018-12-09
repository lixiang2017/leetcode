# no loop for 2


class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5

        return int(num) & int(num - 1) == 0


if __name__ == "__main__":
    num = 1
    assert Solution().isUgly(num)
    num = 2
    assert Solution().isUgly(num)
    num = 3
    assert Solution().isUgly(num)
    num = 5
    assert Solution().isUgly(num)
    num = 30
    assert Solution().isUgly(num)
    num = -45
    assert not Solution().isUgly(num)
    num = 0
    assert not Solution().isUgly(num)
    num = 14
    assert not Solution().isUgly(num)