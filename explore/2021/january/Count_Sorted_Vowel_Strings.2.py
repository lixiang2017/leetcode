'''
approach: backtracking + memoization

41 / 41 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 13.4 MB
Submitted: 0 minutes ago

You are here!
Your runtime beats 28.42 % of python submissions.
You are here!
Your memory usage beats 71.23 % of python submissions.
'''


class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.backtracking(["a","e","i","o","u"], [], n, 1)
    
    memo = {} 
    # key: (current_vowel, left_vowels_to_add)
    # value: count
    
    def backtracking(self, vowels, path, n, count):
        if len(path) == n:
            return count
        
        if path and (path[-1], n - len(path)) in self.memo:
            return self.memo[(path[-1], n - len(path))]
        
        child_count = 0
        for vowel in vowels:
            if (path and ord(path[-1]) <= ord(vowel)) or (not path):
                # child_count += self.backtracking(vowels, path + [vowel], n, count)
                if (vowel, n - len(path) - 1) not in self.memo:
                    self.memo[(vowel, n - len(path) - 1)] = self.backtracking(vowels, path + [vowel], n, count)
                child_count += self.memo[(vowel, n - len(path) - 1)]
        
        if path and (path[-1], n - len(path)) not in self.memo:
            self.memo[(path[-1], n - len(path))] = child_count
            
        return child_count
