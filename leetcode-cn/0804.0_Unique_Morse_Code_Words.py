'''
hash table

执行用时：36 ms, 在所有 Python3 提交中击败了68.72% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了76.36% 的用户
通过测试用例：82 / 82
'''
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
            "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
            ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        for word in words:
            t = ''.join(morse[ord(ch) - ord('a')] for ch in word)
            trans.add(t)
        return len(trans)

'''
hash set
执行用时：40 ms, 在所有 Python3 提交中击败了49.51% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了84.60% 的用户
通过测试用例：82 / 82
'''
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        for w in words:
            trans.add(''.join(morse[ord(ch) - ord('a')] for ch in w))
        return len(trans)
