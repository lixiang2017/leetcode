'''
BFS - Bidirectional

You are here!
Your runtime beats 96.93 % of python submissions.
You are here!
Your memory usage beats 13.11 % of python submissions.
'''

from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        self.all_combo_dict = defaultdict(list)
    
    def visitWordNode(self, queque, visited, others_visited):
        current_word, level = queque.popleft()
        for i in range(self.length):
            intermediate_word = current_word[: i] + '*' + current_word[i + 1:]
            
            for word in self.all_combo_dict[intermediate_word]:
                if word in others_visited:
                    return level + others_visited[word]
                
                if word not in visited:
                    visited[word] = level + 1
                    queque.append((word, level + 1))
        
        return None
        
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                intermediate = word[: i] + '*' + word[i + 1: ]
                self.all_combo_dict[intermediate].append(word)
        
        queque_begin = deque([(beginWord, 1)])
        queque_end = deque([(endWord, 1)])
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        
        while queque_begin and queque_end:
            # one hop from begin word
            ans = self.visitWordNode(queque_begin, visited_begin, visited_end)
            if ans:
                return ans
            # one hop from end word
            ans = self.visitWordNode(queque_end, visited_end, visited_begin)
            if ans:
                return ans
        
        return 0
        