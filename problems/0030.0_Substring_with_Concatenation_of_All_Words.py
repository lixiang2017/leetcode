'''
brute force

151 / 178 test cases passed.
    Status: Memory Limit Exceeded
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        choice = set()
        for p in permutations(words):
            choice.add(''.join(p))
        m = sum(len(w) for w in words)
        n = len(s)
        ans = []
        for i in range(n - m + 1):
            if s[i: i + m] in choice:
                ans.append(i)
        return ans 

'''
hash table

Runtime: 1056 ms, faster than 34.69% of Python3 online submissions for Substring with Concatenation of All Words.
Memory Usage: 14.9 MB, less than 9.15% of Python3 online submissions for Substring with Concatenation of All Words.
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c = Counter(words)
        k = len(words[0])
        wc = len(words)
        hit_indice = set()
        n = len(s)
        for i in range(n - k + 1):
            # n - k, n
            if s[i: i + k] in c:
                hit_indice.add(i)
        ans = []
        
        def check(i):
            c1 = Counter()
            for j in range(i, i + k * wc, k):
                if j not in hit_indice:
                    return False
                w = s[j: j + k] 
                c1[w] += 1
                if c1[w] > c[w]:
                    return False
            return True
        
        for i in range(n - len(words) * k + 1):
            # n - len(words) * k, n
            if check(i):
                ans.append(i)
        return ans 
    

