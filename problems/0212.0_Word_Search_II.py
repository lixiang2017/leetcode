'''
Trie + Backtracking

Runtime: 8464 ms, faster than 21.70% of Python3 online submissions for Word Search II.
Memory Usage: 14.8 MB, less than 18.18% of Python3 online submissions for Word Search II.
'''
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None

class Trie:
    def __init__(self):
        self.t = TrieNode()
    
    def add(self, word):
        t = self.t
        for ch in word:
            t = t.children[ch]
        t.word = word
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()
        for word in words:
            t.add(word)
        
        M, N = len(board), len(board[0])
        ans = []
        def dfs(i, j, trie, l):
            if l > 10 or board[i][j] not in trie.children:
                return
            ch = board[i][j]
            nxt = trie.children[board[i][j]]
            if nxt.word:
                ans.append(nxt.word)
                nxt.word = None
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N:
                    board[i][j] = '#'
                    dfs(ni, nj, nxt, l + 1)
                    board[i][j] = ch      
        
        for x in range(M):
            for y in range(N):
                dfs(x, y, t.t, 0)     
        return ans
