'''
Author: lixiang
Beats: 99.69%
Solution: recursion
'''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        s = self.countAndSay(n-1)
        ret = ""
        l = len(s)
        if l > 0:
            c = s[0]
            count = 1
            for i in range(1, l):
                if c == s[i]:
                    count += 1
                else:
                    ret += str(count) + c
                    c = s[i]
                    count = 1
        ret += str(count) + s[-1::1]
        return ret
            


if __name__ == "__main__":
    n = 1
    print(Solution().countAndSay(n))

    n = 2
    print(Solution().countAndSay(n))

    n = 5
    print(Solution().countAndSay(n))

#    for i in range(1, 31):
#        print(i, ' : ', "'",Solution().countAndSay(i), "',", sep = '')