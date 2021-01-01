'''
Success
Details
Runtime: 76 ms, faster than 26.49% of Python online submissions for Longest Substring with At Least K Repeating Characters.
Memory Usage: 13.6 MB, less than 70.86% of Python online submissions for Longest Substring with At Least K Repeating Characters.


Approach 3: Sliding Window

Intuition

There is another intuitive method to solve the problem by using the Sliding Window Approach. The sliding window slides over the string s and validates each character. Based on certain conditions, the sliding window either expands or shrinks.

A substring is valid if each character has at least k frequency. The main idea is to find all the valid substrings with a different number of unique characters and track the maximum length. Let's look at the algorithm in detail.

Algorithm

    Find the number of unique characters in the string s and store the count in variable maxUnique. For s = aabcbacad, the unique characters are a,b,c,d and maxUnique = 4.

    Iterate over the string s with the value of currUnique ranging from 1 to maxUnique. In each iteration, currUnique is the maximum number of unique characters that must be present in the sliding window.

    The sliding window starts at index windowStart and ends at index windowEnd and slides over string s until windowEnd reaches the end of string s. At any given point, we shrink or expand the window to ensure that the number of unique characters is not greater than currUnique.

    If the number of unique character in the sliding window is less than or equal to currUnique, expand the window from the right by adding a character to the end of the window given by windowEnd

    Otherwise, shrink the window from the left by removing a character from the start of the window given by windowStart.

    Keep track of the number of unique characters in the current sliding window having at least k frequency given by countAtLeastK. Update the result if all the characters in the window have at least k frequency.


Complexity Analysis

    Time Complexity : O(maxUnique⋅N)\mathcal{O}(\text{maxUnique} \cdot N)O(maxUnique⋅N). We iterate over the string of length NNN, maxUnqiue\text{maxUnqiue}maxUnqiue times. Ideally, the number of unique characters in the string would not be more than 262626 (a to z). Hence, the time complexity is approximately O(26⋅N)\mathcal{O}( 26 \cdot N)O(26⋅N) = O(N)\mathcal{O}(N)O(N)

    Space Complexity: O(1)\mathcal{O}(1)O(1) We use constant extra space of size 26 to store the countMap.

'''

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        size = len(s)
        # countMap = [0 for _ in range(26)]
        maxUnique = len(set(s))
        longest_length = 0
        for currUnique in range(1, maxUnique + 1):
            countMap = [0 for _ in range(26)]
            windowStart = windowEnd = idx = unique = countAtLeastK = 0
            while windowEnd < size:
                # expand the sliding window
                if unique <= currUnique:
                    idx = ord(s[windowEnd]) - ord('a')
                    if countMap[idx] == 0: unique += 1
                    countMap[idx] += 1
                    if countMap[idx] == k: countAtLeastK += 1
                    windowEnd += 1
                # shrink the sliding window
                else:
                    idx = ord(s[windowStart]) - ord('a')
                    if countMap[idx] == k: countAtLeastK -= 1
                    countMap[idx] -= 1
                    if countMap[idx] == 0: unique -= 1
                    windowStart += 1
                if unique == currUnique and unique == countAtLeastK:
                    longest_length = max(windowEnd - windowStart, longest_length)
        
        return longest_length
    
    
        
        
