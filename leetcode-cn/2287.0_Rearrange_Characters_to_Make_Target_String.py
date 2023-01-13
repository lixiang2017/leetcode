'''
hash table

执行用时：32 ms, 在所有 Python3 提交中击败了88.66% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了41.24% 的用户
通过测试用例：115 / 115
'''
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc, tc = Counter(s), Counter(target)
        ans = inf
        for ch, need in tc.items():
            ans = min(ans, sc[ch] // need)
        return ans 
