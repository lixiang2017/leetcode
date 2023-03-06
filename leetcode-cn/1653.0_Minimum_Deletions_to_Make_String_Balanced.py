'''
执行用时：660 ms, 在所有 Python3 提交中击败了37.69% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了98.46% 的用户
通过测试用例：157 / 157
'''
class Solution:
    def minimumDeletions(self, s: str) -> int:
        s = 'a' + s 
        total_a = 0
        for ch in s:
            if ch == 'a':
                total_a += 1
        total_b = len(s) - total_a
        ans = len(s)
        cur_a = cur_b = 0
        for ch in s:
            if ch == 'a':
                cur_a += 1
            else:
                cur_b += 1
            ans = min(ans, total_a - cur_a + cur_b)
        return ans 

'''
0x3f

执行用时：228 ms, 在所有 Python3 提交中击败了90.00% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了98.46% 的用户
通过测试用例：157 / 157
'''
class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = delete = s.count('a')
        for c in s:
            delete -= 1 if c == 'a' else -1
            if delete < ans:
                ans = delete
        return ans


'''
0x3f

执行用时：368 ms, 在所有 Python3 提交中击败了67.69% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：157 / 157
炫耀一下:
'''
class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = cnt_b = 0
        for ch in s:
            if ch == 'a':
                dp = min(dp + 1, cnt_b)
            else:
                cnt_b += 1
        return dp
