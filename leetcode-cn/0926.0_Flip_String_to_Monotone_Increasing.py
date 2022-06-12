'''
T: O(2N) = O(N)
S: O(1)

执行用时：268 ms, 在所有 Python3 提交中击败了61.22% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了76.87% 的用户
通过测试用例：93 / 93
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        cnt = Counter(s)
        ans = min(cnt['0'], cnt['1'])
        zero = one = 0
        for ch in s:
            if ch == '0':
                zero += 1
            else:
                one += 1
            # left 1 -> 0, right 0 -> 1
            left = one
            right = cnt['0'] - zero 
            ans = min(ans, left + right)
        return ans 
