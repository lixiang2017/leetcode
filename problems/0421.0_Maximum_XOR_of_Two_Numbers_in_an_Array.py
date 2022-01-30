'''
Runtime: 4263 ms, faster than 36.01% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
Memory Usage: 91.6 MB, less than 55.28% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
'''
'''

                    ^
                  0   1
               0  1   0  1
             0 1  ......  0 1               
               
               
2 ^ 31 - 1: 31 个 1
'''

class Trie:
    def __init__(self):
        self.t = dict()
    
    def add(self, x):
        t = self.t
        for i in range(30, -1, -1):
            # 0 or 1
            b = (1 << i) & x
            bit = 1 if b else 0
            if bit not in t:
                t[bit] = dict()
            t = t[bit]
        

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = Trie()
        for x in nums:
            t.add(x)
        ans = 0
        
        def dfs(t1, t2, value):
            nonlocal ans
            if not t1 or not t2:
                ans = max(ans, value)
                return
            if (0 in t1 and 1 in t2) or (1 in t1 and 0 in t2):
                if 0 in t1 and 1 in t2:
                    dfs(t1[0], t2[1], value * 2 + 1)
                if 1 in t1 and 0 in t2:
                    dfs(t1[1], t2[0], value * 2 + 1)
            else:
                if 0 in t1 and 0 in t2:
                    dfs(t1[0], t2[0], value * 2)
                if 1 in t1 and 1 in t2:
                    dfs(t1[1], t2[1], value * 2)
        
        dfs(t.t, t.t, 0)
        return ans
    
'''
[3,10,5,25,2,8]
[14,70,53,83,49,91,36,80,92,51,66,70]
[32,18,33,42,29,20,26,36,15,46]
'''
    
    
