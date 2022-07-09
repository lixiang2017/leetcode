'''
Trie

执行用时：68 ms, 在所有 Python3 提交中击败了87.76% 的用户
内存消耗：29.7 MB, 在所有 Python3 提交中击败了35.97% 的用户
通过测试用例：126 / 126
'''
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        for root in dictionary:
            t = trie 
            for ch in root:
                t = t[ch]
            t['#'] = root

        replaced = []
        for word in sentence.split():
            t = trie 
            Found = False
            for ch in word:
                if '#' in t:
                    Found = True
                    replaced.append(t['#'])
                    break 
                if ch in t:
                    t = t[ch]
                else:
                    break
            if not Found:
                replaced.append(word)

        return ' '.join(replaced)


'''
brute force

执行用时：124 ms, 在所有 Python3 提交中击败了67.99% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了70.62% 的用户
通过测试用例：126 / 126
'''
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        replaced = []
        for word in sentence.split():
            changed = word 
            for root in dictionary:
                if word.startswith(root) and len(changed) > len(root):
                    changed = root 
            replaced.append(changed)
        return ' '.join(replaced)

