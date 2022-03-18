'''
hash table
T: O(N)
S: O(52)

执行用时：40 ms, 在所有 Python3 提交中击败了42.98% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了65.82% 的用户
通过测试用例：95 / 95
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        isSingle = False
        for ch, c in cnt.items():
            ans += (c // 2) * 2
            if c % 2:
                isSingle = True 
                
        return ans + isSingle
