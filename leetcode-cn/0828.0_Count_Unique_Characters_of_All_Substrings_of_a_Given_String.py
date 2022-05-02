'''
DP
计算贡献
T: O(3N)
S: O(2N)

执行用时：336 ms, 在所有 Python3 提交中击败了44.64% 的用户
内存消耗：23.2 MB, 在所有 Python3 提交中击败了5.36% 的用户
通过测试用例：76 / 76
'''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        left, right = [-1] * n, [n] * n
        pos = dict()
        for i, ch in enumerate(s):
            if ch in pos:
                left[i] = pos[ch]
            pos[ch] = i
            
        pos = dict()
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch in pos:
                right[i] = pos[ch]
            pos[ch] = i 

        ans = 0
        for i in range(n):
            ans += (i - left[i]) * (right[i] - i)
        return ans 
