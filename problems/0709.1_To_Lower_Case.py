'''
Runtime: 49 ms, faster than 18.41% of Python3 online submissions for To Lower Case.
Memory Usage: 14.3 MB, less than 36.99% of Python3 online submissions for To Lower Case.
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()



'''
Runtime: 32 ms, faster than 69.03% of Python3 online submissions for To Lower Case.
Memory Usage: 14.4 MB, less than 5.13% of Python3 online submissions for To Lower Case.
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        
        def lower(ch):
            if ord('a') <= ord(ch) <= ord('z'):
                return ch
            elif ord('A') <= ord(ch) <= ord('Z'):
                return chr(ord(ch) - ord('A') + ord('a'))
            else:
                return ch
    
        return ''.join(lower(ch) for ch in s)

    
'''
Input
"al&phaBET"
Output
"alFphabet"
Expected
"al&phabet"
'''
