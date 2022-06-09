'''
Runtime: 48 ms, faster than 26.24% of Python3 online submissions for Remove Palindromic Subsequences.
Memory Usage: 13.9 MB, less than 10.77% of Python3 online submissions for Remove Palindromic Subsequences.
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        if n < 1:
            return 0
        
        def isPalindrome(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False 
                i += 1
                j -= 1
            return True 
        
        return 2 - int(isPalindrome(0, n - 1)) 


'''
Runtime: 52 ms, faster than 18.23% of Python3 online submissions for Remove Palindromic Subsequences.
Memory Usage: 13.8 MB, less than 96.13% of Python3 online submissions for Remove Palindromic Subsequences.
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - int(s == s[:: -1]) 


'''
Runtime: 48 ms, faster than 26.24% of Python3 online submissions for Remove Palindromic Subsequences.
Memory Usage: 13.8 MB, less than 53.87% of Python3 online submissions for Remove Palindromic Subsequences.
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[:: -1]) - (s == '')
        