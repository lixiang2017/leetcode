'''
Approach: Two Pointer

Complexity Analysis
 Time Complexity: O(N), where N is the length of S.
 Space Complexity: O(N), the space used by the answer.

Success
Details 
Runtime: 24 ms, faster than 75.84% of Python online submissions for Positions of Large Groups.
Memory Usage: 13.4 MB, less than 42.70% of Python online submissions for Positions of Large Groups.
'''

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        groups = []
        
        i = j = 0
        size = len(s)
        while i < size and j < size:
            # start = i
            j = i + 1
            while j < size and s[j] == s[i]:
                j += 1
            if j - 1 - i >= 2:
                groups.append([i, j - 1])
                  
            i = max(j - 1, i + 1)  # to avoid TLE
        
        return groups
