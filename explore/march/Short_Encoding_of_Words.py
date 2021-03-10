'''
approach: Reverse + Sort
Time: O(NlogN)
Space: O(1)

You are here!
Your memory usage beats 93.33 % of python submissions.
'''


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted([word[:: -1] for word in words])
        N, length = len(words), 0
        for i in range(N - 1):
            size = len(words[i])
            if words[i] == words[i + 1][:size]:
                continue
            length += size + 1
        
        return length + len(words[-1]) + 1

'''
approach: Reverse + Sort + Reverse
Time: O(NlogN)
Space: O(1)

Runtime: 92 ms, faster than 76.67% of Python online submissions for Short Encoding of Words.
Memory Usage: 14 MB, less than 86.67% of Python online submissions for Short Encoding of Words.
'''

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = sorted([word[:: -1] for word in words])[::-1]
        length = 0
        wordsNum = len(words)
        wordsIdx = 0
        while (wordsIdx < wordsNum):
            word = words[wordsIdx]
            while (wordsIdx + 1 < wordsNum):
                if not word.startswith(words[wordsIdx + 1]):
                    break
                wordsIdx += 1
            length += len(word) + 1
            wordsIdx += 1
            
        return length



'''
approach: Hash Set, Store Longest Suffixes
Time: O(sigma w[i]^2), which w[i] is the length of word and every word has w[i] suffixes.
For every suffix, we will do w[i] hash calculation.
Space: O(sigma w[i])

You are here!
Your memory usage beats 70.00 % of python submissions.
'''


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        distinct = set(words)
        for word in words:
            for i in range(1, len(word)):
                distinct.discard(word[i:])
        
        return sum(len(word) + 1 for word in distinct)


'''
approach: Trie
'''

class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        trie = Node()
        nodes = []
        for word in words:
            now = trie
            for w in reversed(word):
                if w in now.children:
                    now = now.children[w]
                else:
                    now.children[w] = Node()
                    now = now.children[w]
            nodes.append(now)
        
        return sum(len(word) + 1 for word, node in zip(words, nodes) if len(node.children) == 0)
        
        
        
class Node(object):
    def __init__(self):
        self.children = {}


'''
approach: Trie

ref:
https://leetcode-cn.com/problems/short-encoding-of-words/solution/dan-ci-de-ya-suo-bian-ma-by-leetcode-solution/

You are here!
Your memory usage beats 33.33 % of python submissions.
'''
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        trie = {}
        nodes = []
        for word in words:
            now = trie
            for w in reversed(word):
                if w in now:
                    now = now[w]
                else:
                    now[w] = {}
                    now = now[w]
            nodes.append(now)
        
        return sum(len(word) + 1 for word, node in zip(words, nodes) if len(node) == 0)
        
        

'''
approach: Trie
You are here!
Your memory usage beats 40.00 % of python submissions.
'''
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words = set(words)
        Trie = lambda : collections.defaultdict(Trie)
        trie = Trie()
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)




'''
approach: Trie
You are here!
Your runtime beats 42.44 % of python3 submissions.
You are here!
Your memory usage beats 20.35 % of python3 submissions.
'''
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        Trie = lambda : collections.defaultdict(Trie)
        trie = Trie()
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)
                


