'''
Trie + Backtracking + Sort

执行用时：1024 ms, 在所有 Python3 提交中击败了74.00% 的用户
内存消耗：38.3 MB, 在所有 Python3 提交中击败了35.00% 的用户
通过测试用例：44 / 44
'''
class Trie:
    def __init__(self):
        self.nxt = {}
        self.end = False 
    def insert(self, s):
        cur = self 
        for ch in s:
            if ch not in cur.nxt:
                cur.nxt[ch] = Trie()
            cur = cur.nxt[ch]
        cur.end = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def backtrace(s, idx, cnt, n):
            if idx == n:
                return cnt > 1
            cur = trie 
            for i in range(idx, n):
                if s[i] not in cur.nxt:
                    break 
                cur = cur.nxt[s[i]]
                if cur.end and backtrace(s, i + 1, cnt + 1, n):
                    return True 
            return False 
        
        trie = Trie()
        ans = []
        for s in sorted(words, key=len):
            if backtrace(s, 0, 0, len(s)):
                ans.append(s)
            else:
                trie.insert(s)
        return ans 


