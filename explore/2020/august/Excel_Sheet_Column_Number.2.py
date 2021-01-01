'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/
You are here!
Your runtime beats 63.18 % of python submissions.
1000 / 1000 test cases passed.
    Status: Accepted
Runtime: 24 ms
Memory Usage: 13 MB
    
Submitted: 0 minutes ago

'''



class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        d = {chr(n): n - ord('A') + 1 for n in xrange(ord('A'), ord('Z') + 1)}
        # print d
        for i in xrange(len(s)):
            c = s[i]            
            ans = ans * 26 + d[c]

        return ans
        

if __name__ == '__main__':
    s = 'A'
    assert Solution().titleToNumber(s) == 1

    s = 'AB'
    assert Solution().titleToNumber(s) == 28

    s = 'ZY'
    assert Solution().titleToNumber(s) == 701

    s = 'FXSHRXW'
    print Solution().titleToNumber(s) # 2147483647