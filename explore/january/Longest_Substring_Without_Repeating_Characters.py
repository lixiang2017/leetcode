'''
Time: O(N^3)
Space: O(1)

You are here!
Your runtime beats 8.08 % of python submissions.
You are here!
Your memory usage beats 7.10 % of python submissions.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        total = len(s)
        for i in range(total):
            for j in range(i, total):
                if s[j] not in s[i: j]:
                    # print 'i, j: ', i, j
                    longest = max(j - i + 1, longest)
                    # print longest
                else:
                    break
        return longest