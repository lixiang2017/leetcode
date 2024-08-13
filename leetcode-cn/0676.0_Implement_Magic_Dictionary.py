'''
执行用时：164 ms, 在所有 Python3 提交中击败了67.55% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了80.85% 的用户
通过测试用例：83 / 83
'''
class MagicDictionary:

    def __init__(self):
        self.dict = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict = dictionary

    def search(self, searchWord: str) -> bool:
        for d in self.dict:
            if len(d) != len(searchWord):
                continue
            if 1 == sum(a != b for a, b in zip(d, searchWord)):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)



class MagicDictionary:

    def __init__(self):
        self.len2words = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.len2words[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.len2words[len(searchWord)]:
            if sum(a != b for a, b in zip(word, searchWord)) == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


'''
Trie
'''
class MagicDictionary:

    def __init__(self):
        t =  lambda: defaultdict(t)
        self.trie = t()
        self.word = ""

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            t = self.trie 
            for ch in word:
                t = t[ch]
            t["#"] = 1

    def search(self, searchWord: str) -> bool:
        self.word = searchWord
        return self.compare(0, self.trie, 0)
    
    def compare(self, index: int, trie: dict, diff: int) -> bool:
        if index == len(self.word) and "#" in trie and diff == 1:
            return True
        if index >= len(self.word) or diff > 1:
            return False
        ret = False
        ch = self.word[index]
        for ch1 in trie:
            if "#" == ch1:
                continue
            if ch == ch1:
                ret |= self.compare(index + 1, trie[ch1], diff)
            else:
                ret |= self.compare(index + 1, trie[ch1], diff + 1)
        return ret 

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


