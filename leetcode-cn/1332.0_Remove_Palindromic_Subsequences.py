'''
执行用时：36 ms, 在所有 Python3 提交中击败了33.92% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了64.33% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[:: -1] else 2


'''
执行用时：36 ms, 在所有 Python3 提交中击败了33.92% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了21.64% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindromic(s):
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        return 1 if isPalindromic(s) else 2


'''
执行用时：32 ms, 在所有 Python3 提交中击败了65.50% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了36.26% 的用户
通过测试用例：48 / 48
'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindromic(s):
            l, r = 0, len(s) - 1
            while l <= r and s[l] == s[r]:
                l += 1
                r -= 1

            return l > r

        return 1 if isPalindromic(s) else 2




