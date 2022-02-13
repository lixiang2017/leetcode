'''
BFS

Runtime: 213 ms, faster than 14.19% of Python3 online submissions for Word Ladder II.
Memory Usage: 14.6 MB, less than 71.47% of Python3 online submissions for Word Ladder II.
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set()
        for word in wordList:
            word_set.add(word)
        if endWord not in word_set:
            return []
        
        q = deque([ [beginWord, [beginWord]] ])   
        l = len(beginWord)
        seen = set([beginWord])
        while q:
            next_q = deque()
            ans = []
            visited = seen.copy()
            for word, arr in q:
                for i in range(l):
                    for low in string.ascii_lowercase:
                        com = word[: i] + low + word[i + 1: ]
                        if com in word_set:
                            if com == endWord:
                                ans.append(arr + [com])
                            else:
                                if com not in visited:
                                    next_q.append([com, arr + [com]])
                                    seen.add(com)
            if ans:
                return ans
            else:
                q = next_q

        return []    
