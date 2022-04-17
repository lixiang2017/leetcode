'''

执行用时：48 ms, 在所有 Python3 提交中击败了18.20% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了82.43% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;. "
        pattern = "!|\?|'|,|;|\.| "
        ban_set = set(banned)
        ans, cnt = '', 0
        counter = Counter()
        for word in re.split(pattern, paragraph):
            w = word.strip(symbols).lower()
            if w and w not in ban_set:
                counter[w] += 1
                if counter[w] > cnt:
                    cnt = counter[w]
                    ans = w 
        return ans 


'''
执行用时：56 ms, 在所有 Python3 提交中击败了8.16% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了48.12% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = "!|\?|'|,|;|\.| "
        ban_set = set(banned)
        cnt = Counter([w.lower() for w in re.split(pattern, paragraph) if w and w.lower() not in ban_set])
        return cnt.most_common(1)[0][0]


'''
执行用时：32 ms, 在所有 Python3 提交中击败了89.33% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了89.54% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = "!|\?|'|,|;|\.| "
        ban_set = set(banned)
        cnt = Counter([w.lower() for w in re.split(pattern, paragraph) if w and w.lower() not in ban_set])
        return max(cnt, key=cnt.get)


'''
执行用时：44 ms, 在所有 Python3 提交中击败了36.71% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了90.74% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ws = [w for w in re.findall('\w+', paragraph.lower()) if w not in set(banned)]
        return Counter(ws).most_common(1)[0][0]
     

'''
执行用时：52 ms, 在所有 Python3 提交中击败了14.07% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.38% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def more_than_lower(ch):
            # to_lower()
            # filter symbols: "!?',;.", change them to space
            if ord('A') <= ord(ch) <= ord('Z'):
                return chr(ord(ch) - ord('A') + ord('a')) 
            elif ord('a') <= ord(ch) <= ord('z'):
                return ch 
            else:
                return ' '

        para = ''.join(more_than_lower(ch) for ch in paragraph)
        banned_set = set(banned)
        words = [w for w in para.split() if w not in banned_set]
        freq = Counter(words)
        return max(freq, key=freq.get)


'''
尾部加上 + ' t'，免得最后再讨论

执行用时：44 ms, 在所有 Python3 提交中击败了36.71% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了55.75% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def transform(ch):
            # to_lower()
            # filter symbols: "!?',;.", change them to space
            if ord('A') <= ord(ch) <= ord('Z'):
                return chr(ord(ch) - ord('A') + ord('a')) 
            elif ord('a') <= ord(ch) <= ord('z'):
                return ch 
            else:
                return ' '

        freq = Counter()
        ban = set(banned)
        ans, max_cnt = '', 0
        word = ''
        for ch in paragraph + ' t':
            ch = transform(ch)
            if ch != ' ':
                word += ch 
            elif word:
                if word not in ban:
                    freq[word] += 1
                    if freq[word] > max_cnt:
                        max_cnt = freq[word]
                        ans = word
                # clear
                word = ''

        return ans 


'''
执行用时：44 ms, 在所有 Python3 提交中击败了36.71% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了90.39% 的用户
通过测试用例：47 / 47
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word = ''
        wordDict = defaultdict(int)
        for ch in paragraph + ' t':
            if ch.isalpha():
                word += ch.lower()
            elif word != '':
                wordDict[word] += 1
                word = ''
        for ban in banned:
            wordDict.pop(ban, None)

        return max(wordDict, key=wordDict.get)  

        


