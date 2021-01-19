'''
BFS - Single directional


Success
Details
Runtime: 108 ms, faster than 77.91% of Python online submissions for Word Ladder.
Memory Usage: 18.5 MB, less than 12.12% of Python online submissions for Word Ladder.

ref:
https://leetcode.com/problems/word-ladder/solution/
'''


from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not endWord: return 0
        
        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                intermediate = word[:i] + '*' + word[i + 1:]
                all_combo_dict[intermediate].append(word)
        
        curs = deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while curs:
            curWord, level = curs.popleft()
            if curWord == endWord:
                return level
            
            for i in range(L):
                intermediate = curWord[:i] + '*' + curWord[i + 1:]
                for word in all_combo_dict[intermediate]:
                    if word not in visited:
                        curs.append((word, level + 1))
                        visited[word] = True
                
        return 0
            
