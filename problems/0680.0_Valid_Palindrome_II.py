'''
two pointers
T: O(N)
S: O(1)

类似的题，只是改成链表了
https://leetcode-cn.com/contest/cnunionpay-2022spring/problems/D7rekZ/

Runtime: 164 ms, faster than 65.01% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 14.5 MB, less than 91.68% of Python3 online submissions for Valid Palindrome II.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        
        def check(x, y):
            while x < y:
                if s[x] == s[y]:
                    x += 1
                    y -= 1
                else:
                    return False
            return True
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return check(i, j - 1) or check(i + 1, j)
        return True
