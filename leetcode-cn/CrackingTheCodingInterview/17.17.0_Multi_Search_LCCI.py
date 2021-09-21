'''
Brute Force
T: O(10^8)

执行用时：360 ms, 在所有 Python3 提交中击败了42.61% 的用户
内存消耗：34.4 MB, 在所有 Python3 提交中击败了28.41% 的用户
通过测试用例：32 / 32
'''
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:

        def f(s):
            if not s:
                return []
            cur = []
            idx = big.find(s)
            while idx >= 0:
                # yield idx
                cur.append(idx)
                idx = big.find(s, idx + 1)
            return cur

        return [f(s) for s in smalls]


'''
Trie

执行用时：232 ms, 在所有 Python3 提交中击败了68.75% 的用户
内存消耗：32.8 MB, 在所有 Python3 提交中击败了67.61% 的用户
通过测试用例：32 / 32
'''
class Trie:
    def __init__(self, words):
        self.d = {}
        for word in words:
            t = self.d
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            # 因为Trie里每个孩子都是一个小写字母,所以这里用'end'不影响
            t['end'] = word
    
    def search(self, str):
        t = self.d
        res = []
        for ch in str:
            if ch not in t:
                break
            t = t[ch]
            if 'end' in t:
                res.append(t['end'])
        return res

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = Trie(smalls)
        hit = defaultdict(list)
        for i in range(len(big)):
            matches = trie.search(big[i: ])
            for m in matches:
                hit[m].append(i)

        return [hit[s] for s in smalls]

