'''
一开始想的用 Trie, 后来一想没必要，直接 hash table 就行。

执行用时：5056 ms, 在所有 Python3 提交中击败了5.02% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了8.80% 的用户
通过测试用例：177 / 177
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ns, nw, L = len(s), len(words), len(words[0])
        word2indice = defaultdict(list)
        for i, w in enumerate(words):
            word2indice[w].append(i)
        ans = []
        # try to start from every position
        for i in range(ns):
            got = []
            # seen word, word -> index of indice
            seen = defaultdict(int)
            for k in range(nw):
                part = s[i + L * k: i + L * k + L]
                if part not in word2indice:
                    break 
                indice = word2indice[part]
                if seen[part] >= len(indice):
                    break 
                got.append(indice[seen[part]])
                seen[part] += 1

            if len(got) == nw:
                ans.append(i)

        return ans 


'''
for i in range(ns - nw * L + 1)

执行用时：460 ms, 在所有 Python3 提交中击败了58.18% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了6.00% 的用户
通过测试用例：177 / 177
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ns, nw, L = len(s), len(words), len(words[0])
        word2indice = defaultdict(list)
        for i, w in enumerate(words):
            word2indice[w].append(i)
        ans = []
        # try to start from every position
        for i in range(ns - nw * L + 1):
            got = []
            # seen word, word -> index of indice
            seen = defaultdict(int)
            for k in range(nw):
                part = s[i + L * k: i + L * k + L]
                if part not in word2indice:
                    break 
                indice = word2indice[part]
                if seen[part] >= len(indice):
                    break 
                got.append(indice[seen[part]])
                seen[part] += 1

            if len(got) == nw:
                ans.append(i)

        return ans 



'''
word_cnt, got_cnt
只需计数即可，不用记录下标位置

执行用时：428 ms, 在所有 Python3 提交中击败了61.35% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了98.60% 的用户
通过测试用例：177 / 177
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ns, nw, L = len(s), len(words), len(words[0])
        word_cnt = defaultdict(int)
        for i, w in enumerate(words):
            word_cnt[w] += 1
        ans = []
        # try to start from every position
        for i in range(ns - nw * L + 1):
            got_cnt = 0
            # seen word count
            seen = defaultdict(int)
            for k in range(nw):
                part = s[i + L * k: i + L * k + L]
                if part not in word_cnt:
                    break 
                cnt = word_cnt[part]
                if seen[part] >= cnt:
                    break 
                got_cnt += 1
                seen[part] += 1

            if got_cnt == nw:
                ans.append(i)

        return ans 



'''
word_cnt = Counter(words)

执行用时：388 ms, 在所有 Python3 提交中击败了64.72% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了97.82% 的用户
通过测试用例：177 / 177
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ns, nw, L = len(s), len(words), len(words[0])
        word_cnt = Counter(words)
        ans = []
        # try to start from every position
        for i in range(ns - nw * L + 1):
            got_cnt = 0
            # seen word count
            seen = defaultdict(int)
            for k in range(nw):
                part = s[i + L * k: i + L * k + L]
                if part not in word_cnt:
                    break 
                cnt = word_cnt[part]
                if seen[part] >= cnt:
                    break 
                got_cnt += 1
                seen[part] += 1

            if got_cnt == nw:
                ans.append(i)

        return ans 
