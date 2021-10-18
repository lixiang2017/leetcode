'''
Trie

执行用时：204 ms, 在所有 Python3 提交中击败了74.76% 的用户
内存消耗：30.5 MB, 在所有 Python3 提交中击败了18.36% 的用户
通过测试用例：13 / 13
'''
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = None

class WordDictionary:

    def __init__(self):
        self.t = Trie()

    def addWord(self, word: str) -> None:
        t = self.t 
        for ch in word:
            t = t.children[ch]
        t.word = word

    def search(self, word: str) -> bool:
        t = self.t
        choice = [t]
        for ch in word:
            next_choice = []
            if not choice:
                return False
            for c in choice:
                if ch != '.' and ch in c.children:
                    next_choice += [c.children[ch]]
                elif ch == '.':
                    next_choice += c.children.values()

            choice = next_choice

        return any(c.word for c in choice)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
