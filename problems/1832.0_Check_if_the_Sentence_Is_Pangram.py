'''
hash set

Runtime: 59 ms, faster than 43.23% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 13.9 MB, less than 11.66% of Python3 online submissions for Check if the Sentence Is Pangram.
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return 26 == len(set(sentence))


'''
bitmask

Runtime: 78 ms, faster than 5.29% of Python3 online submissions for Check if the Sentence Is Pangram.
Memory Usage: 13.8 MB, less than 54.73% of Python3 online submissions for Check if the Sentence Is Pangram.
'''
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        x = 0
        for ch in sentence:
            x |= 1 << (ord(ch) - ord('a'))
        return x == (1 << 26) - 1
