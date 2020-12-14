'''
Approach: backtracking

Success
Details
Runtime: 664 ms, faster than 5.21% of Python online submissions for Palindrome Partitioning.
Memory Usage: 27.3 MB, less than 7.29% of Python online submissions for Palindrome Partitioning.

Time: O(N * 2 ^ N)
Space: O(N)
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        currentList = []
        self.dfs(result, s, 0, currentList)
        return result
        
        
    def dfs(self, result, s, start, currentList):
        if start >= len(s):
            # print currentList
            result.append(currentList)
            # print 'result: ', result
            return 
        
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                # add current substring in the currentList
                # currentList.append(s[start: end + 1])  # result will be []
                self.dfs(result, s, end + 1, currentList + [s[start: end + 1]])
                # backtrack and remove the current substring from currentList
                # currentList.pop()   # no need
    
    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
