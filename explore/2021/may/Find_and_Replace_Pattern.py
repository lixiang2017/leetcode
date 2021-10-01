'''
approach: Hash Table * 2
Time: O(N*W)
Space: O(2*W) = O(W)

You are here!
Your runtime beats 90.19 % of python3 submissions.
You are here!
Your memory usage beats 58.99 % of python3 submissions.
'''



class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matched = []
        for word in words:
            if self.match(word, pattern):
                matched.append(word)
        
        return matched

    def match(self, word: str, pattern: str) -> bool:
        w2p, p2w = {}, {}
        for w, p in zip(word, pattern):
            if w in w2p and p in p2w:
                if w2p[w] == p and p2w[p] == w:
                    continue
                else:
                    return False
            elif w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            else:
                return False
        
        return True


'''
approach: Hash Table * 2
Time: O(N*W)
Space: O(2*W) = O(W)

You are here!
Your runtime beats 90.19 % of python3 submissions
You are here!
Your memory usage beats 58.99 % of python3 submissions.
'''

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:        
        return [word for word in words if self.match(word, pattern)]

    def match(self, word: str, pattern: str) -> bool:
        w2p, p2w = {}, {}
        for w, p in zip(word, pattern):
            if w in w2p and p in p2w:
                if w2p[w] == p and p2w[p] == w:
                    continue
                else:
                    return False
            elif w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            else:
                return False
        
        return True



'''
approach: Hash Table * 2
Time: O(N*W)
Space: O(2*W) = O(W)

Runtime: 32 ms, faster than 67.57% of Python3 online submissions for Find and Replace Pattern.
Memory Usage: 14.4 MB, less than 5.31% of Python3 online submissions for Find and Replace Pattern.
'''

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:        
        arg = [[word, pattern] for word in words]
        return [word for word, pattern in list(filter(self.match, arg))]

    def match(self, word_pattern: list) -> bool:
        word, pattern = word_pattern
        w2p, p2w = {}, {}
        for w, p in zip(word, pattern):
            if w in w2p and p in p2w:
                if w2p[w] == p and p2w[p] == w:
                    continue
                else:
                    return False
            elif w not in w2p and p not in p2w:
                w2p[w] = p
                p2w[p] = w
            else:
                return False
        
        return True