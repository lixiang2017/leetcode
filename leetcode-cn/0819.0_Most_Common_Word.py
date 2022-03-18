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


