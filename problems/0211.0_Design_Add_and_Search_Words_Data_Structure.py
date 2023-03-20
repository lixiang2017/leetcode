'''
Trie + DFS

Runtime: 332 ms, faster than 66.58% of Python3 online submissions for Design Add and Search Words Data Structure.
Memory Usage: 25.5 MB, less than 62.35% of Python3 online submissions for Design Add and Search Words Data Structure.
'''
class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = dict()
            t = t[ch]
        t['end'] = True
        

    def search(self, word: str) -> bool:
        def dfs(t: dict, part: str) -> bool:
            for i, ch in enumerate(part):
                if ch == '.':
                    check = False
                    for child in t:
                        if child != 'end':
                            check |= dfs(t[child], part[i + 1: ])
                    return check
                elif ch in t:
                    t = t[ch]
                else:
                    return False
            return 'end' in t
        
        return dfs(self.trie, word)
    
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


'''
Trie + DFS

Runtime: 437 ms, faster than 32.57% of Python3 online submissions for Design Add and Search Words Data Structure.
Memory Usage: 25.4 MB, less than 62.69% of Python3 online submissions for Design Add and Search Words Data Structure.
'''
class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        t = self.trie
        for ch in word:
            t = t.setdefault(ch, {})
        t['end'] = True
        

    def search(self, word: str) -> bool:
        def dfs(t: dict, part: str) -> bool:
            for i, ch in enumerate(part):
                if ch == '.':
                    return any(dfs(t[child], part[i + 1: ]) for child in t if child != 'end')
                elif ch in t:
                    t = t[ch]
                else:
                    return False
            return 'end' in t
        
        return dfs(self.trie, word)
    
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


'''
Trie + DFS

Runtime: 6579 ms, faster than 88.84% of Python3 online submissions for Design Add and Search Words Data Structure.
Memory Usage: 58 MB, less than 79.13% of Python3 online submissions for Design Add and Search Words Data Structure.
'''
T = lambda : defaultdict(T)

class WordDictionary:

    def __init__(self):
        self.t = T()        

    def addWord(self, word: str) -> None:
        t = self.t
        for ch in word:
            t = t[ch]
        t['#'] = True

    def search(self, word: str) -> bool:
        n = len(word)
        
        def dfs(i: int, t: dict) -> bool:
            if i == n:
                return '#' in t
            
            if word[i] == '.':
                Found = False
                for ch in t:
                    if ch == '#':
                        continue
                    Found |= dfs(i + 1, t[ch])
                    if Found:
                        return True
                return Found
            else:
                return word[i] in t and dfs(i + 1, t[word[i]])
        
        return dfs(0, self.t)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


'''
Trie + BFS

Runtime: 5832 ms, faster than 90.54% of Python3 online submissions for Design Add and Search Words Data Structure.
Memory Usage: 58.2 MB, less than 78.93% of Python3 online submissions for Design Add and Search Words Data Structure.
'''
T = lambda : defaultdict(T)

class WordDictionary:

    def __init__(self):
        self.t = T()        

    def addWord(self, word: str) -> None:
        t = self.t
        for ch in word:
            t = t[ch]
        t['#'] = True

    def search(self, word: str) -> bool:
        n = len(word)
        
        q = [self.t]
        for i in range(n):
            next_q = []
            for t in q:
                if word[i] == '.':
                    for ch in t:
                        if ch == '#':
                            continue
                        next_q.append(t[ch])
                else:
                    if word[i] in t:
                        next_q.append(t[word[i]])
            if not next_q:
                return False
            q = next_q
        
        return any('#' in t for t in q)
            
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


