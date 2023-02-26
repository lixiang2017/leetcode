'''
执行用时：216 ms, 在所有 Python3 提交中击败了46.84% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了83.54% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        pocket = [0] * 26
        for ch in letters:
            pocket[ord(ch) - ord('a')] += 1
        word_score = [0] * n 
        for i, word in enumerate(words):
            word_score[i] = sum(score[ord(ch) - ord('a')] for ch in word)

        def formable_score(mask):
            s = 0
            char_cnt = [0] * 26
            for i in range(n):
                if (mask >> i) & 1:
                    for ch in words[i]:
                        idx = ord(ch) - ord('a')
                        char_cnt[idx] += 1
                        if char_cnt[idx] > pocket[idx]:
                            return 0
                    s += word_score[i]
            return s 

        ans = 0
        for mask in range((1 << n) - 1, 0, -1):
            s = formable_score(mask)
            ans = max(ans, s)
        return ans 
        
        