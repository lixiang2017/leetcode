'''
suf + '#' + pre, Trie

执行用时：1304 ms, 在所有 Python3 提交中击败了21.88% 的用户
内存消耗：83.8 MB, 在所有 Python3 提交中击败了15.63% 的用户
通过测试用例：13 / 13
'''
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.idx = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.t = Trie()
        for idx, w in enumerate(words):
            for i in range(len(w)):
                suf_pre = w[i: ] + '#' + w
                self.add(suf_pre, idx)
    
    def add(self, word: str, idx: int):
        t = self.t 
        found_pre = False
        for ch in word:
            if not found_pre and ch == '#':
                found_pre = True            
            t = t.children[ch]
            if found_pre:
                t.idx = max(t.idx, idx)

    def f(self, prefix: str, suffix: str) -> int:
        suf_pre = suffix + '#' + prefix
        t = self.t
        for ch in suf_pre:
            t = t.children[ch]
        return t.idx

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)



'''
执行用时：740 ms, 在所有 Python3 提交中击败了72.31% 的用户
内存消耗：46.8 MB, 在所有 Python3 提交中击败了49.23% 的用户
通过测试用例：13 / 13
'''
class WordFilter:

    def __init__(self, words: List[str]):
        indices = {}
        for idx, w in enumerate(words):
            for prei in range(len(w) + 1):
                pre = w[: prei]
                for posti in range(len(w) + 1):
                    post = w[posti: ]
                    indices[(pre, post)] = idx
        self.indices = indices

    def f(self, prefix: str, suffix: str) -> int:
        return self.indices.get((prefix, suffix), -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
