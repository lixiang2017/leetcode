'''
Divide and Conquer

https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solution/

Complexity Analysis

    Time Complexity : O(N2)\mathcal{O}(N ^ {2})O(N2), where NNN is the length of string sss. Though the algorithm performs better in most cases, the worst case time complexity is still O(N2)\mathcal{O}(N ^ {2})O(N2).

In cases where we perform split at every index, the maximum depth of recursive call could be O(N)\mathcal{O}(N)O(N). For each recursive call it takes O(N)\mathcal{O}(N)O(N) time to build the countMap resulting in O(n2)\mathcal{O}(n ^ {2})O(n2) time complexity.

    Space Complexity: O(N)\mathcal{O}(N)O(N) This is the space used to store the recursive call stack. The maximum depth of recursive call stack would be O(N)\mathcal{O}(N)O(N).



You are here!
Your runtime beats 91.06 % of python submissions.
'''

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        size = len(s)
        return self.longestSubstringUtil(s, 0, size, k)

        
    def longestSubstringUtil(self, s, start, end, k):
        if end < k: return 0
        countMap = [0 for _ in range(26)]
        # update the countMap with the count of each character
        for i in range(start, end):
            countMap[ord(s[i]) - ord('a')] += 1
        for mid in range(start, end):
            if countMap[ord(s[mid]) - ord('a')] >= k: continue
            midNext = mid + 1
            while (midNext < end and countMap[ord(s[midNext]) - ord('a')] < k): midNext += 1
            return max(self.longestSubstringUtil(s, start, mid, k),  \
                      self.longestSubstringUtil(s, midNext, end, k))
        
        return end - start 
    
    
        
        
