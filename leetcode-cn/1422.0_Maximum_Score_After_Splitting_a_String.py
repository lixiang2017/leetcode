'''
执行用时：56 ms, 在所有 Python3 提交中击败了9.42% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.42% 的用户
通过测试用例：104 / 104
'''
class Solution:
    def maxScore(self, s: str) -> int:
        c = Counter(s)
        zero = one = ans = 0
        for i, ch in enumerate(s):
            if i == len(s) - 1:
                break 
            if ch == '0':
                zero += 1
            else:
                one += 1
            ans = max(ans, zero + c['1'] - one)
        return ans 
        