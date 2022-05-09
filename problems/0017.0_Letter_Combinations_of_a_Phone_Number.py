'''
iteration

Runtime: 37 ms, faster than 67.10% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 31.84% of Python3 online submissions for Letter Combinations of a Phone Number.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if 0 == n:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = ['']
        for d in digits:
            ans = [a + p for a in ans for p in phone[d]]
        return ans 


'''
backtrack

Runtime: 62 ms, faster than 8.64% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 79.68% of Python3 online submissions for Letter Combinations of a Phone Number.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if 0 == n:
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = ['']
        
        def backtrack(i: int):
            nonlocal ans, n
            if i >= n:
                return 
            d = digits[i]
            ans = [a + p for a in ans for p in phone[d]]
            backtrack(i + 1)
            
        backtrack(0)
        return ans 
    


