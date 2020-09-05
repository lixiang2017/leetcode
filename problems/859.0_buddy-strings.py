#
# @lc app=leetcode id=859 lang=python
#
# [859] Buddy Strings
#
'''
Accepted
23/23 cases passed (28 ms)
Your runtime beats 24.68 % of python submissions
Your memory usage beats 33.33 % of python submissions (13.5 MB)
'''


# @lc code=start
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        diff = [(a, b) for (a, b) in zip(A, B) if a != b]
        return 2 == len(diff) and diff[0] == diff[1][::-1]
        
# @lc code=end


if __name__ == '__main__':
    A = "ab"
    B = "ba"
    assert Solution().buddyStrings(A, B) == True

    A = "ab"
    B = "ab"
    assert Solution().buddyStrings(A, B) == False

    A = "aa"
    B = "aa"
    assert Solution().buddyStrings(A, B) == True
    
    A = "aaaaaaabc"
    B = "aaaaaaacb"
    assert Solution().buddyStrings(A, B) == True

    A = ""
    B = "aa"
    assert Solution().buddyStrings(A, B) == False

