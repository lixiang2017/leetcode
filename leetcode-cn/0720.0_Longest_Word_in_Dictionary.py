'''
hash table

执行用时：60 ms, 在所有 Python3 提交中击败了50.74% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了33.42% 的用户
通过测试用例：59 / 59
'''
class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans, max_len = '', 0
        memo, candidate = defaultdict(set), defaultdict(set)
        for word in words:
            max_len = max(max_len, len(word))
            memo[len(word)].add(word)

        candidate[0].add('')
        for i in range(1, max_len + 1):
            if not candidate[i - 1]:
                break
            for cand in candidate[i - 1]:
                for ch in string.ascii_lowercase:
                    compose = cand + ch
                    if compose in memo[i]:
                        candidate[i].add(compose)
                        if len(compose) > len(ans) or (len(compose) == len(ans) and compose < ans):
                            ans = compose

        return ans
