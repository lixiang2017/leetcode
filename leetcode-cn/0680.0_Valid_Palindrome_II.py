'''
two pointers, T:O(N), S: O(1)

执行用时：144 ms, 在所有 Python3 提交中击败了35.31% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了71.20% 的用户
通过测试用例：467 / 467
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True 
            
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return check(i + 1, j) or check(i, j - 1)

        return True


'''
执行用时：96 ms, 在所有 Python3 提交中击败了73.96% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了51.08% 的用户
通过测试用例：467 / 467
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # return check(i + 1, j) or check(i, j - 1)
                return s[i+1: j+1] == s[i+1: j+1][:: -1] or s[i: j] == s[i: j][:: -1]

        return True
