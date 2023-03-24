'''
Trie

执行用时：420 ms, 在所有 Python3 提交中击败了68.85% 的用户
内存消耗：45.6 MB, 在所有 Python3 提交中击败了45.90% 的用户
通过测试用例：18 / 18
'''
T = lambda: defaultdict(T)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = T()
        for word in words:
            t = self.t 
            for ch in reversed(word):
                t = t[ch]
            t['#'] = True
        self.q = []
        self.m = max(len(word) for word in words)

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        t = self.t
        n = len(self.q)
        i = n - 1
        step = 0
        while i >= 0 and step <= self.m + 1:
            if '#' in t:
                return True
            elif self.q[i] in t:
                t = t[self.q[i]]
                i -= 1
                step += 1
            else:
                break

        return '#' in t

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
