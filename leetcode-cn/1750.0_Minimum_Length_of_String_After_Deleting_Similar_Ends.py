'''
two pointers
T: O(N)
S: O(1)

执行用时：84 ms, 在所有 Python3 提交中击败了68.49% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了63.01% 的用户
通过测试用例：100 / 100
'''
class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            ii = i 
            i += 1
            while i < j and s[i] == s[ii]:
                i += 1
            jj = j
            j -= 1 
            while i <= j and s[j] == s[jj]:
                j -= 1
        return j - i + 1
            
