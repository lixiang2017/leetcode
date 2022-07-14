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





'''
p, s = self.preTrie, self.sufTrie + list + two pointers

Trie = lambda: defaultdict(Trie) 必须放在 __init__ 函数里面。如果放在 class variables 里就会有问题。

执行用时：1256 ms, 在所有 Python3 提交中击败了40.62% 的用户
内存消耗：52.3 MB, 在所有 Python3 提交中击败了52.08% 的用户
通过测试用例：17 / 17
'''
class WordFilter:

    def __init__(self, words: List[str]):
        Trie = lambda: defaultdict(Trie)
        self.preTrie = Trie()
        self.sufTrie = Trie()

        for i, word in enumerate(words):
            p, s = self.preTrie, self.sufTrie
            for ch in word:
                p = p[ch]
                if 'idx' not in p:
                    p['idx'] = [i]
                else:
                    p['idx'].append(i)
            for ch in word[:: -1]:
                s = s[ch]
                if 'idx' not in s:
                    s['idx'] = [i]
                else:
                    s['idx'].append(i)

    def f(self, pref: str, suff: str) -> int:
        p, s = self.preTrie, self.sufTrie
        for ch in pref:
            if ch in p:
                p = p[ch]
            else:
                return -1
        for ch in suff[:: -1]:
            if ch in s:
                s = s[ch]
            else:
                return -1
        # two pointers to find max index
        p_indice = p['idx']
        s_indice = s['idx']
        i, j = len(p_indice) - 1, len(s_indice) - 1
        while i >= 0 and j >= 0:
            if p_indice[i] == s_indice[j]:
                return  p_indice[i]
            elif p_indice[i] > s_indice[j]:
                i -= 1
            elif p_indice[i] < s_indice[j]:
                j -= 1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)



'''
p, s = self.preTrie, self.sufTrie + list + two pointers + cache

执行用时：1212 ms, 在所有 Python3 提交中击败了43.75% 的用户
内存消耗：53.8 MB, 在所有 Python3 提交中击败了50.00% 的用户
通过测试用例：17 / 17
'''
class WordFilter:

    def __init__(self, words: List[str]):
        Trie = lambda: defaultdict(Trie)
        self.preTrie = Trie()
        self.sufTrie = Trie()
        self.cache = {}

        for i, word in enumerate(words):
            p, s = self.preTrie, self.sufTrie
            for ch in word:
                p = p[ch]
                if 'idx' not in p:
                    p['idx'] = [i]
                else:
                    p['idx'].append(i)
            for ch in word[:: -1]:
                s = s[ch]
                if 'idx' not in s:
                    s['idx'] = [i]
                else:
                    s['idx'].append(i)

    def f(self, pref: str, suff: str) -> int:
        if (pref, suff) in self.cache:
            return self.cache[(pref, suff)]
        p, s = self.preTrie, self.sufTrie
        for ch in pref:
            if ch in p:
                p = p[ch]
            else:
                self.cache[(pref, suff)] = -1
                return -1
        for ch in suff[:: -1]:
            if ch in s:
                s = s[ch]
            else:
                self.cache[(pref, suff)] = -1
                return -1
        # two pointers to find max index
        p_indice = p['idx']
        s_indice = s['idx']
        i, j = len(p_indice) - 1, len(s_indice) - 1
        while i >= 0 and j >= 0:
            if p_indice[i] == s_indice[j]:
                self.cache[(pref, suff)] = p_indice[i]
                return  p_indice[i]
            elif p_indice[i] > s_indice[j]:
                i -= 1
            elif p_indice[i] < s_indice[j]:
                j -= 1
        self.cache[(pref, suff)] = -1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)




