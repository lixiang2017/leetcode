'''
T: O(N^2)
S: O(N)

Runtime: 743 ms, faster than 66.77% of Python3 online submissions for Maximum Product of Word Lengths.
Memory Usage: 14.1 MB, less than 99.05% of Python3 online submissions for Maximum Product of Word Lengths.
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        mask = [0] * n
        for i, w in enumerate(words):
            for ch in w:
                mask[i] |= (1 << (ord(ch) - ord('a')))
        
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if 0 == mask[i] & mask[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans 
    
'''
使用 hash table 优化，去重记录并记录同一个 mask value 对应的最长 word length
T: O(N^2)
S: O(N)

Runtime: 518 ms, faster than 80.54% of Python3 online submissions for Maximum Product of Word Lengths.
Memory Usage: 14.3 MB, less than 93.67% of Python3 online submissions for Maximum Product of Word Lengths.
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        # mask_value -> word len
        mask = defaultdict(int)
        for w in words:
            m = 0
            for ch in w:
                m |= (1 << (ord(ch) - ord('a')))
            mask[m] = max(mask[m], len(w))
        
        ans = 0
        for m1, l1 in mask.items():
            for m2, l2 in mask.items():
                if m1 & m2 == 0:
                    ans = max(ans, l1 * l2)
        return ans 


'''
使用 combinations(mask, 2) 优化
T: O(N^2)
S: O(N)

Runtime: 307 ms, faster than 93.04% of Python3 online submissions for Maximum Product of Word Lengths.
Memory Usage: 14.4 MB, less than 42.09% of Python3 online submissions for Maximum Product of Word Lengths.
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        # mask_value -> word len
        mask = defaultdict(int)
        for w in words:
            m = 0
            for ch in w:
                m |= (1 << (ord(ch) - ord('a')))
            mask[m] = max(mask[m], len(w))
        
        ans = 0
        for m1, m2 in combinations(mask, 2):
            if m1 & m2 == 0:
                ans = max(ans, mask[m1] * mask[m2])
        return ans 
    





