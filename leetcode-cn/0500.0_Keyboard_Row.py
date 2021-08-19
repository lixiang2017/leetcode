'''
Hash Table

执行用时：32 ms, 在所有 Python3 提交中击败了79.13% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.35% 的用户
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {f: 1 for f in chain("qwertyuiop", "qwertyuiop".upper())}
        second = {s: 2 for s in chain("asdfghjkl", "asdfghjkl".upper())}
        third = {t: 3 for t in chain("zxcvbnm", "zxcvbnm".upper())}
        alpha = first | second | third
        ans = []
        for word in words:
            row = set(alpha[w] for w in word)
            if len(row) == 1:
                ans.append(word)
        return ans


'''
strip

执行用时：32 ms, 在所有 Python3 提交中击败了79.13% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了79.31% 的用户
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for W in words:
            w = W.lower()
            if w.strip("qwertyuiop") == '' or w.strip("asdfghjkl") == '' or w.strip("zxcvbnm") == '':
                ans.append(W)
        return ans
