'''
approach: Hash Table
Time: O(1)
Space: O(words * word.len^2)

You are here!
Your runtime beats 83.55 % of python3 submissions.
You are here!
Your memory usage beats 51.97 % of python3 submissions.
'''

class WordFilter:

    def __init__(self, words: List[str]):
        self.memo = {}
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                for k in range(len(word) + 1):
                    now = word[: j] + '$' + word[k: ]
                    self.memo[now] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.memo.get(prefix + '$' + suffix, -1)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


'''
["WordFilter","f"]
[[["apple"]],["a","e"]]
["WordFilter","f", "f", "f"]
[[["appindex", "appwordat", "appfilrat", "appcustat"]],["app","at"], ["app","dat"], ["app","x"]]
["WordFilter","f","f","f","f","f","f","f","f","f","f"]
[[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]

["WordFilter","f"]
[[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["ac","accabaccaa"]]
'''