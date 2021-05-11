'''

Time: O( (M*N)^N ), where M is the length of each word and N is the total number of words in the input word list.

22 / 43 test cases passed.
    Status: Time Limit Exceeded
    
Submitted: 0 minutes ago
Last executed input: "qa"
"sq"
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

'''

import copy

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0
        
        
        def backtracking(transWord, endWord, wordList, stepsList, steps, transList, transformation):
            if transWord == endWord:
                stepsList.append(steps)
                transList.append(transformation)
            
            for word in wordList:
                if self.diffLength(word, transWord) == 1:
                    newWordList = copy.deepcopy(wordList)
                    newWordList.remove(word)
                    print 'transformation: ', transformation
                    print 'newWordList: ', newWordList

                    backtracking(word, endWord, newWordList, stepsList, steps + 1, transList, transformation + [word])
            
            return stepsList, transList
        
        stepsList, transList = backtracking(beginWord, endWord, wordList, stepsList = [], steps = 0, transList = [], transformation = [])
        print stepsList
        print transList
        if not stepsList:
            return 0
        else:
            return min(stepsList) + 1
            
    def diffLength(self, OneWord, AnotherWord):
        diff = 0
        for one, two in zip(OneWord, AnotherWord):
            if one != two:
                diff += 1
        return diff


if __name__ == '__main__':
    beginWord = "qa"
    endWord = "sq"
    wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]

    Solution().ladderLength(beginWord, endWord, wordList)

'''
'qa' -> ['ca', 'ba', 'ra', 'fa', 'ya', 'ma', 'ga', 'ha', 'qa', 'na', 'la', 'ta', 'pa']  # word.endswith('a')
'sq' -> ['si', 'se', 'so', 'sb', 'sm', 'sn', 'sr', 'sh', 'st', 'sc', 'sq']   # word.startswith('s')

qa -> gz -> go -> so -> sq
qa -> la -> ln -> sn -> sq

'''