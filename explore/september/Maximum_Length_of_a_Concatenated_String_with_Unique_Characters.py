'''
DFS
T: O(sigma + 2^N), sigma is the sum length of all strings in the given ``arr``.
S: O(N)

You are here!
Your runtime beats 42.69 % of python3 submissions.
You are here!
Your memory usage beats 63.33 % of python3 submissions.
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [a for a in arr if len(set(a)) == len(a)]
        N = len(arr)
        ans = 0
        
        # idx, mask
        def dfs(i, mask):
            nonlocal ans
            ans = max(ans, bin(mask).count('1'))       
            if i >= N:
                return 
            
            dfs(i + 1, mask)
            m = getMask(arr[i])
            if mask & m == 0:
                dfs(i + 1, mask | m)
        
        def getMask(word):
            m = 0
            for ch in word:
                m |= 1 << (ord(ch) - ord('a'))
            return m
        
        dfs(0, 0)
        return ans

'''
DFS
T: O(sigma + 2^N)
S: O(N)

You are here!
Your runtime beats 19.10 % of python3 submissions.
You are here!
Your memory usage beats 92.12 % of python3 submissions.
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # arr = [a for a in arr if len(set(a)) == len(a)]
        N = len(arr)
        ans = 0
        
        # idx, mask
        def dfs(i, mask):
            nonlocal ans
            ans = max(ans, bin(mask).count('1'))       
            if i >= N:
                return 
            
            dfs(i + 1, mask)
            m = getMask(arr[i])
            if mask & m == 0:
                dfs(i + 1, mask | m)
        
        def getMask(word):
            m = 0
            for ch in word:
                if m & (1 << (ord(ch) - ord('a'))):
                    return 0
                m |= 1 << (ord(ch) - ord('a'))
            return m
        
        dfs(0, 0)
        return ans



'''
Iteration
T: O(sigma + 2^N)
S: O(2^N)

You are here!
Your runtime beats 97.05 % of python3 submissions.
You are here!
Your memory usage beats 40.71 % of python3 submissions.
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def getMask(word):
            m = 0
            for ch in word:
                i = ord(ch) - ord('a')
                if ((m >> i) & 1):
                    return 0
                m |= 1 << i
            return m
        
        ans = 0
        masks = [0]
        for s in arr:
            m = getMask(s)
            if 0 == m: continue
            n = len(masks)
            for i in range(n):
                if masks[i] & m:
                    continue
                ans = max(ans, bin(masks[i] | m).count('1'))
                masks.append(masks[i] | m)
        
        return ans




