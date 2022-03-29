'''
two pointers, T: O(N), S:O(1)

执行用时：88 ms, 在所有 Python3 提交中击败了5.70% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了73.67% 的用户
通过测试用例：480 / 480
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def isAlphanumeric(idx):
            # Alphanumeric characters include letters and numbers.
            return ord('A') <= ord(s[idx]) <= ord('Z') \
                or ord('a') <= ord(s[idx]) <= ord('z') \
                or ord('0') <= ord(s[idx]) <= ord('9')

        while i < j:
            while i < j and not isAlphanumeric(i):
                i += 1
            ch1 = s[i].lower()    

            while i < j and not isAlphanumeric(j):
                j -= 1
            ch2 = s[j].lower()
            if ch1 != ch2:
                return False
            i += 1
            j -= 1

        return True
