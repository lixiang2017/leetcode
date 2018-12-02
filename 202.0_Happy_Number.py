'''
Author: lixiang
Beats: 43.39% -> 80.99%
'''
class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = []
        s = str(n)
        while True:
            sum = 0
            for i in s:
                sum += int(i) ** 2
            if sum == 1:
                return True
            elif sum in res:
                return False
            else:
                res.append(sum)
                s = str(sum)

if __name__ == "__main__":
    n = 19
    assert Solution().isHappy(n)
    n = 1
    assert Solution().isHappy(n)
    n = 9
    assert not Solution().isHappy(n)