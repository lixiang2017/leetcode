'''
Your code took 1523 milliseconds — faster than 27.55% in Python
'''
class Solution:
    def solve(self, words):
        def mask(w):
            m = 0
            for ch in w:
                m |= 1<< (ord(ch) - ord('a'))
            return m, len(w)
        
        masks = [mask(w) for w in words]
        ans = 0
        for a, b in permutations(masks, 2):
            if a[0] & b[0] == 0:
                ans = max(ans, a[1] + b[1])
        return ans
        



'''
按长度降序排列，减少比较次数。

Your code took 1311 milliseconds — faster than 44.39% in Python
'''
class Solution:
    def solve(self, words):
        words.sort(key=len, reverse=True)
        words_len = [len(w) for w in words]
        words_set = [set(w) for w in words]
        N = len(words)

        ans = 0
        for i in range(N):
            for j in range(i, N):
                if words_len[i] + words_len[j] < ans:
                    break
                if next((ch for ch in words_set[i] if ch in words_set[j]), None) is None:
                    ans = max(ans, words_len[i] + words_len[j])
        return ans


'''
两种方法综合一下。

Success!
Your code took 850 milliseconds — faster than 80.61% in Python
'''
class Solution:
    def solve(self, words):
        words.sort(key=len, reverse=True)
        words_len = [len(w) for w in words]

        def mask(w):
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - ord('a'))
            return m

        masks = [mask(w) for w in words]
        N = len(words)

        ans = 0
        for i in range(N):
            for j in range(i, N):
                if words_len[i] + words_len[j] < ans:
                    break
                if masks[i] & masks[j] == 0:
                    ans = max(ans, words_len[i] + words_len[j])
        return ans
