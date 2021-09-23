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



'''
ref:
https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solution/gong-shui-san-xie-yi-ti-san-jie-jian-zhi-nfeb/

You are here!
Your runtime beats 99.94 % of python3 submissions.
You are here!
Your memory usage beats 62.79 % of python3 submissions.
'''
class Solution:
    # num -> bit count
    num2len = {}
    
    def lowbit(self, x):
        return x & -x
    
    # get bit count
    def getCount(self, cur):
        if cur in self.num2len:
            return self.num2len[cur]
        c = 0
        while cur:
            c += 1
            cur -= self.lowbit(cur)
        self.num2len[cur] = c
        return c
    
    def getMask(self, word):
        m = 0
        for ch in word:
            i = ord(ch) - ord('a')
            if ((m >> i) & 1):
                return 0
            m |= 1 << i
        return m
    
    def maxLength(self, arr: List[str]) -> int:
        from operator import or_
        # distinct masks
        masks = [m for x in arr if (m := self.getMask(x)) != 0]
        if not masks:
            return 0
        N = len(masks)
        ans = 0
        total = bin(reduce(or_, masks)).count('1')
        
        # idx_in_masks, cur_mask
        def dfs(i, cur):
            nonlocal ans
            if total <= ans:
                return
            if i >= N:
                ans = max(ans, self.getCount(cur))
                return 
            if cur & masks[i] == 0:
                dfs(i + 1, cur | masks[i])
            
            # not pick
            dfs(i + 1, cur)
        
        dfs(0, 0)
        return ans
    
'''

Runtime Error Message: TypeError: reduce() of empty sequence with no initial value
    total = bin(reduce(or_, masks)).count('1')
Line 34 in maxLength (Solution.py)
    ret = Solution().maxLength(param_1)
Line 71 in _driver (Solution.py)
    _driver()
Line 82 in <module> (Solution.py)
Last executed input: ["yy","bkhwmpbiisbldzknpm"]
'''
        
'''
ref:
https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/solution/gong-shui-san-xie-yi-ti-san-jie-jian-zhi-nfeb/

85 / 85 test cases passed.
    Status: Accepted
Runtime: 2556 ms
Memory Usage: 14 MB

You are here!
Your memory usage beats 99.74 % of python3 submissions.
'''
class Solution:
    # num -> bit count
    num2len = {}
    
    def lowbit(self, x):
        return x & -x
    
    # get bit count
    def getCount(self, cur):
        if cur in self.num2len:
            return self.num2len[cur]
        c = 0
        while cur:
            c += 1
            cur -= self.lowbit(cur)
        self.num2len[cur] = c
        return c
    
    def getMask(self, word):
        m = 0
        for ch in word:
            i = ord(ch) - ord('a')
            if ((m >> i) & 1):
                return 0
            m |= 1 << i
        return m
    
    def maxLength(self, arr: List[str]) -> int:
        from operator import or_
        # distinct masks
        masks = [m for x in arr if (m := self.getMask(x)) != 0]
        if not masks:
            return 0
        N = len(masks)
        ans = 0
        for i in range(1 << N):
            m = count = 0
            for j in range(N):
                if (i >> j) & 1:
                    if m & masks[j] == 0:
                        m |= masks[j]
                        count += self.getCount(masks[j])
                    else:
                        m = 0
                        break
            if m:
                ans = max(ans, count)
        return ans
        










