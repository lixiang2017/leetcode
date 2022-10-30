'''
执行用时：36 ms, 在所有 Python3 提交中击败了96.24% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了77.11% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for ch in s:
            if ch.isdigit():
                ans = [a + ch for a in ans]
            elif 'a' <= ch <= 'z':
                ans1 = [a + ch for a in ans]
                ans2 = [a + chr(ord('A') - ord('a') + ord(ch)) for a in ans]
                ans = ans1 + ans2 
            else:
                ans1 = [a + ch for a in ans]
                ans2 = [a + chr(ord('a') - ord('A') + ord(ch)) for a in ans]
                ans = ans1 + ans2 
        return ans 


'''
chr(32 ^ ord(ch))

执行用时：40 ms, 在所有 Python3 提交中击败了90.03% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了81.99% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for ch in s:
            if ch.isdigit():
                ans = [a + ch for a in ans]
            elif 'a' <= ch <= 'z':
                ans1 = [a + ch for a in ans]
                ans2 = [a + chr(32 ^ ord(ch)) for a in ans]
                ans = ans1 + ans2 
            else:
                ans1 = [a + ch for a in ans]
                ans2 = [a + chr(32 ^ ord(ch)) for a in ans]
                ans = ans1 + ans2 
        return ans 


'''
执行用时：32 ms, 在所有 Python3 提交中击败了98.68% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了73.25% 的用户
通过测试用例：63 / 63
'''
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for ch in s:
            if ch.isdigit():
                ans = [a + ch for a in ans]
            elif 'a' <= ch <= 'z':
                ans1 = [a + ch for a in ans]
                ans2 = [a + ch.swapcase() for a in ans]
                ans = ans1 + ans2 
            else:
                ans1 = [a + ch for a in ans]
                ans2 = [a + ch.swapcase() for a in ans]
                ans = ans1 + ans2 
        return ans 
        