'''
Author: lixiang
Beats: 99.32%
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
    x = 121
    print(Solution().isPalindrome(x))

    x = -121
    print(Solution().isPalindrome(x))

    x = 10
    print(Solution().isPalindrome(x))