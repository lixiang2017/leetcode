'''
执行用时：92 ms, 在所有 Python3 提交中击败了62.01% 的用户
内存消耗：16.6 MB, 在所有 Python3 提交中击败了32.44% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(ch in allowed for ch in w) for w in words)

'''
执行用时：128 ms, 在所有 Python3 提交中击败了21.15% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了6.57% 的用户
通过测试用例：74 / 74
'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        def encode(word):
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord('a')))
            return mask

        a = encode(allowed)
        ans = 0
        for w in words:
            x = encode(w)
            if x & a == x:
                ans += 1
        return ans 
       
       