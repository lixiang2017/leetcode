'''
Brute Force
Time: O(26 * n^2) = O(n^2)
Space: O(1)

Success
Details
Runtime: 9240 ms, faster than 5.30% of Python online submissions for Longest Substring with At Least K Repeating Characters.
Memory Usage: 14.1 MB, less than 9.93% of Python online submissions for Longest Substring with At Least K Repeating Characters.
'''

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest_length = 0
        size = len(s)
        for i in range(size):
            countMap = defaultdict(int)
            for j in range(i, size):
                countMap[s[j]] += 1
                if self.isValid(countMap, k):
                    longest_length = max(longest_length, j - i + 1)
        
        return longest_length
        
    def isValid(self, countMap, k):
        for ch, times in countMap.iteritems():
            if times < k:
                return False
        return True        