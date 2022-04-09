'''
hash table

执行用时：64 ms, 在所有 Python3 提交中击败了82.72% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了25.37% 的用户
通过测试用例：36 / 36
'''
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = [0] * 26
        for ch in chars:
            freq[ord(ch) - ord('a')] += 1
        
        def check(word):
            f = [0] * 26
            for ch in word:
                idx = ord(ch) - ord('a')
                f[idx] += 1
                if f[idx] > freq[idx]:
                    return False
            return True
        
        return sum(len(word) if check(word) else 0 for word in words)

