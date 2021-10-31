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


'''
set

执行用时：32 ms, 在所有 Python3 提交中击败了63.60% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了41.31% 的用户
通过测试用例：22 / 22
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        for W in words:
            w = W.lower()
            setx = set(w)
            if setx <= set1 or setx <= set2 or setx <= set3:
                ans.append(W)
        return ans


'''
re.match

执行用时：32 ms, 在所有 Python3 提交中击败了63.60% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了49.48% 的用户
通过测试用例：22 / 22
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if re.match('^[qwertyuiopQWERTYUIOP]*$', word) or \
            re.match('^[asdfghjklASDFGHJKL]*$', word) or re.match('^[zxcvbnmZXCVBNM]*$', word)]


'''

执行用时：36 ms, 在所有 Python3 提交中击败了30.61% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了5.35% 的用户
通过测试用例：22 / 22
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return list(
            filter(
                lambda word:
                    re.match('^[qwertyuiop]+$', word, re.I) or
                    re.match('^[asdfghjkl]+$', word, re.I) or
                    re.match('^[zxcvbnm]+$', word, re.I),
                words
            )
        )


