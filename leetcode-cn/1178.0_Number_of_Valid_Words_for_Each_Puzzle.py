'''
Brute Force
Time: O(M * N * L1 * L2), where M the is number of words and N is the number of puzzles.
L1 is the length of one word and L2 and the length of one puzzle.
= (10^5 * 10^4 * 50 * 7)
Space: O(N)

9 / 10 个通过测试用例
状态：超出时间限制
提交时间：几秒内
'''


class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        answer = []
        for puzzle in puzzles:
            num = 0
            for word in words:
                if self.isValid(word, puzzle):
                    num += 1
            answer.append(num)

        return answer

    def isValid(self, word, puzzle):
        if puzzle[0] not in word:
            return False
        
        for letter in word:
            if letter not in puzzle:
                return False

        return True


'''
Brute Force + Set

9 / 10 个通过测试用例
状态：超出时间限制
提交时间：几秒内
'''


class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        answer = []
        for puzzle in puzzles:
            num = 0
            for word in words:
                if self.isValid(word, puzzle):
                    num += 1
            answer.append(num)

        return answer

    def isValid(self, word, puzzle):
        word = set(word)
        if puzzle[0] not in word:
            return False
        
        puzzle = set(puzzle)
        for letter in word:
            if letter not in puzzle:
                return False

        return True
