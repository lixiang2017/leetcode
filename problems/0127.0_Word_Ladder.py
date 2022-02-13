'''
BFS

Runtime: 109 ms, faster than 97.62% of Python3 online submissions for Word Ladder.
Memory Usage: 14.9 MB, less than 96.90% of Python3 online submissions for Word Ladder.
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set()
        for word in wordList:
            word_set.add(word)
        if endWord not in word_set:
            return 0
        seen = set([beginWord])
        one, other = set([beginWord]), set([endWord])
        step, l = 1, len(beginWord)
        while one and other:
            if len(one) > len(other):
                one, other = other, one
            next_one = set()
            for word in one:
                for i in range(l):
                    for low in string.ascii_lowercase:
                        com = word[: i] + low + word[i + 1: ]
                        if com in other:
                            return step + 1
                        else:
                            if com in word_set and com not in seen:
                                next_one.add(com)
                                seen.add(com)
            one = next_one
            step += 1
        
        return 0
