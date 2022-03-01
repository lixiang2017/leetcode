'''
Runtime: 114 ms, faster than 65.10% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 87.66% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]


'''
Runtime: 132 ms, faster than 51.11% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 52.29% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count('1') for i in range(n + 1)]

'''
dfs + memo

Runtime: 119 ms, faster than 61.01% of Python3 online submissions for Counting Bits.
Memory Usage: 25.9 MB, less than 20.83% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = {0: 0, 1: 1}
        
        def dfs(x):
            if x in memo:
                return memo[x]
            if x % 2 == 0:
                memo[x] = dfs(x // 2)
            else:
                memo[x] = dfs(x // 2) + 1
            return memo[x]
        
        for i in range(2, n + 1):
            dfs(i)
            
        return [memo[i] for i in range(n + 1)]
        

'''
iteration
T: O(N)
S: O(1)

Runtime: 114 ms, faster than 65.10% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 87.66% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1  23 4567   89..15
        bc = [0]
        i = 1
        while i <= n:
            if i % 2 == 0:
                bc.append(bc[i // 2])
            else:
                bc.append(bc[i // 2] + 1)
            i += 1
            
        return bc 
   

'''
Runtime: 141 ms, faster than 44.54% of Python3 online submissions for Counting Bits.
Memory Usage: 21 MB, less than 20.83% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1  23 4567   89..15
        bc = [0]
        i = 1
        while i <= n:
            bc.append(bc[i // 2] + (i % 2))
            i += 1
            
        return bc 
    

'''
Runtime: 88 ms, faster than 84.34% of Python3 online submissions for Counting Bits.
Memory Usage: 20.9 MB, less than 20.83% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 1  23 4567   89..15
        bc = [0] * (n + 1)
        for i in range(1, n + 1):
            bc[i] = bc[i >> 1] + (i & 1)
        
        return bc 
    
'''
Runtime: 133 ms, faster than 49.87% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 87.66% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        bc = [0]
        while len(bc) <= n + 1:
            bc.extend([1 + b for b in bc])
        
        return bc[: n + 1]
    
    
'''
Runtime: 131 ms, faster than 51.67% of Python3 online submissions for Counting Bits.
Memory Usage: 20.7 MB, less than 98.20% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        bc = [0]
        while len(bc) <= n + 1:
            bc += [1 + b for b in bc]
        
        return bc[: n + 1]
    

