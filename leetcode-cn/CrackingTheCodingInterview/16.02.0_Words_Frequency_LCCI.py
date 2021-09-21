'''
Hash Table

执行用时：280 ms, 在所有 Python3 提交中击败了63.30% 的用户
内存消耗：43.4 MB, 在所有 Python3 提交中击败了78.11% 的用户
通过测试用例：24 / 24
'''
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.c = Counter(book)

    def get(self, word: str) -> int:
        return self.c[word]

# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
