'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/

481 / 481 test cases passed.
    Status: Accepted
Runtime: 20 ms
Memory Usage: 13.6 MB
    
Submitted: 0 minutes ago


You are here!
Your runtime beats 99.67 % of python submissions.
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        alnum_str = "".join(filter(str.isalnum, str(s))).lower()
        if alnum_str == alnum_str[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    assert Solution().isPalindrome(s)

    s = "race a car"
    assert not Solution().isPalindrome(s)

    s = "race e car"
    assert Solution().isPalindrome(s)

    s = ""
    assert Solution().isPalindrome(s)


'''
TypeError: descriptor 'isalnum' requires a 'str' object but received a 'unicode'
    alnum_str = "".join(filter(str.isalnum, s)).lower()

'''