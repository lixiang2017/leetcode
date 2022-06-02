'''
Rolling Hash
T: O(N)
S: O(2^k)

Runtime: 966 ms, faster than 11.94% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 19 MB, less than 96.46% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        c = k + (1 << k) - 1
        if n < c:
            return False 
        distinct = set()
        x = 0
        for i in range(k):
            x <<= 1
            x += ord(s[i]) - ord('0')
        distinct.add(x)
        for i in range(k, n):
            x -= ( (ord(s[i - k]) - ord('0')) << (k - 1))
            x <<= 1
            x += ord(s[i]) - ord('0')
            distinct.add(x)
        
        return len(distinct) == (1 << k)

'''
早发现，早退出
            if len(distinct) == (1 << k):
                return True
T: O(N)
S: O(2^k)

Runtime: 653 ms, faster than 29.64% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 19.2 MB, less than 95.58% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        c = k + (1 << k) - 1
        if n < c:
            return False 
        distinct = set()
        x = 0
        for i in range(k):
            x <<= 1
            x += ord(s[i]) - ord('0')
        distinct.add(x)
        for i in range(k, n):
            x -= ( (ord(s[i - k]) - ord('0')) << (k - 1))
            x <<= 1
            x += ord(s[i]) - ord('0')
            distinct.add(x)
            if len(distinct) == (1 << k):
                return True
        
        return len(distinct) == (1 << k)


'''
T: O(NK)
S: O(2^k)

Runtime: 597 ms, faster than 37.17% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 27.1 MB, less than 51.77% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        distinct = {s[i - k : i] for i in range(k, n + 1)}    # (n+1) !!!
        return len(distinct) == (1 << k)


'''
Runtime: 535 ms, faster than 47.79% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 22.4 MB, less than 86.73% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = [False] * need 
        all_one = need - 1
        hash_val = 0
    
        for i in range(len(s)):
            hash_val = (((hash_val << 1) & all_one) | int(s[i]))
            if i >= k - 1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if 0 == need:
                    return True
        return False
    

    





