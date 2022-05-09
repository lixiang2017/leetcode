'''
其他答案都是从两端向中间枚举，我这是从中间向两端枚举
T: O(2N)
S: O(1)

执行用时：36 ms, 在所有 Python3 提交中击败了92.04% 的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了33.69% 的用户
通过测试用例：95 / 95
'''

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        freq = Counter(s)
        i_freq, d_freq = freq['I'], freq['D']
        ans = [d_freq]
        l, r = d_freq - 1, d_freq + 1
        for i, ch in enumerate(s):
            if ch == 'D':
                ans.append(l)
                l -= 1
            else:
                ans.append(r)
                r += 1
        return ans 



'''
从两端向中间枚举
T: O(N)
S: O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了40.85% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了99.47% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, r = 0, len(s)
        ans = []
        for ch in s:
            if ch == 'I':
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        ans.append(l)
        return ans 

