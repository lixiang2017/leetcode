'''
two while from the end

执行用时：40 ms, 在所有 Python3 提交中击败了22.53% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了46.13% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while r >= 0 and s[r] == ' ':
            r -= 1
        last = 0
        while r >= 0 and s[r] != ' ':
            last += 1
            r -= 1
        return last


'''
执行用时：32 ms, 在所有 Python3 提交中击败了70.80% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了27.92% 的用户
通过测试用例：58 / 58
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        