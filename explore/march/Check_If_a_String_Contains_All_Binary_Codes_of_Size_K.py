'''
approach: Hash Set
Time: O(N)
Space: O(2 ^ k)

You are here!
Your memory usage beats 70.83 % of python submissions.
'''


class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        N = len(s)
        if N < 2 ** k:
            return False
        
        seen = set()
        for i in range(0, N - k + 1):
            seen.add(s[i: i + k])
        
        if len(seen) == 2 ** k:
            return True
        else:
            return False


'''
approach: Hash Set

Runtime: 228 ms, faster than 91.67% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 45 MB, less than 41.67% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
'''

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        need = 1 << k
        got = set()
        
        for i in range(k, len(s) + 1):
            substr = s[i - k: i]
            if substr not in got:
                got.add(substr)
                need -= 1
                if 0 == need:
                    return True
        return False


'''
approach: Hash Set
Time: O(N * K). We need to iterate the string, and use O(K) to calculate the hash of each substring.
Space: O(N * K). There are at most N strings with length K in the set.

ref:
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solution/

Runtime: 264 ms, faster than 75.00% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 44.9 MB, less than 41.67% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
'''

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        got = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k
    



'''
approach: Rolling Hash
Time: O(N)
Space: O(2^k)

ref:
https://en.wikipedia.org/wiki/Rolling_hash

Runtime: 452 ms, faster than 33.33% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 31.3 MB, less than 79.17% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
'''

class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        need = 1 << k
        got = [False] * need
        all_one = need - 1
        hash_val = 0
        
        for i in range(len(s)):
            # calculate hash for s[i - k + 1: i + 1]
            hash_val = ((hash_val << 1) & all_one | int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k - 1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True
        return False
    

