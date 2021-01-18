'''
38 / 41 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
44
'''


class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.backtracking(["a","e","i","o","u"], [], n, 1)
    
    def backtracking(self, vowels, path, n, count):
        if len(path) == n:
            return count
        
        child_count = 0
        for vowel in vowels:
            if (path and ord(path[-1]) <= ord(vowel)) or (not path):
                child_count += self.backtracking(vowels, path + [vowel], n, count)
                
        return child_count
        