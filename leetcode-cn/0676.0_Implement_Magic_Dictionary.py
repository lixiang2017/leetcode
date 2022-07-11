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
