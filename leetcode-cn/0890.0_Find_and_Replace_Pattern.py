'''
执行用时：40 ms, 在所有 Python3 提交中击败了55.56% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了82.54% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []

        def isMatch(word: str) -> bool:
            if len(word) != len(pattern):
                return False
            w2p, p2w = {}, {}
            for w, p in zip(word, pattern):
                if w not in w2p and p not in p2w:
                    w2p[w] = p
                    p2w[p] = w 
                elif w in w2p and p in p2w:
                    if w2p[w] != p or p2w[p] != w:
                        return False 
                else:
                    return False 
            return True 

        for word in words:
            if isMatch(word):
                ans.append(word)
        return ans 

'''
执行用时：40 ms, 在所有 Python3 提交中击败了55.56% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了16.40% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def isMatch(word: str) -> bool:
            if len(word) != len(pattern):
                return False
            w2p, p2w = {}, {}
            for w, p in zip(word, pattern):
                if w not in w2p and p not in p2w:
                    w2p[w] = p
                    p2w[p] = w 
                elif w in w2p and p in p2w:
                    if w2p[w] != p or p2w[p] != w:
                        return False 
                else:
                    return False 
            return True 

        return list(filter(isMatch, words))


'''
执行用时：36 ms, 在所有 Python3 提交中击败了78.31% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了26.98% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def isMatch(word: str) -> bool:
            if len(word) != len(pattern):
                return False
            return len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern)))

        return list(filter(isMatch, words))


'''
执行用时：40 ms, 在所有 Python3 提交中击败了55.56% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了16.40% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = pattern
        def isMatch(w: str) -> bool:
            return len(w) == len(p) and len(set(w)) == len(set(p)) == len(set(zip(w, p)))

        return list(filter(isMatch, words))


'''
执行用时：32 ms, 在所有 Python3 提交中击败了93.12% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了88.36% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = pattern
        isMatch = lambda w: len(w) == len(p) and len(set(w)) == len(set(p)) == len(set(zip(w, p)))
        return list(filter(isMatch, words))







