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

