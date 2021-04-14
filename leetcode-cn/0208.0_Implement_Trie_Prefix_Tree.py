'''
approach: Dict
Time: O(L), the length of word
Space: O(N), the number of words

执行用时：156 ms, 在所有 Python3 提交中击败了48.36%的用户
内存消耗：28.1 MB, 在所有 Python3 提交中击败了38.21%的用户
'''

from collections import defaultdict

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = defaultdict(dict)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for letter in word:
            if letter in t:
                t = t[letter]
            else:
                t[letter] = defaultdict(dict)
                t = t[letter]
        t['^'] = 1 # end


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for letter in word:
            if letter in t:
                t = t[letter]
            else:
                return False
        return '^' in t

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for letter in prefix:
            if letter in t:
                t = t[letter]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

