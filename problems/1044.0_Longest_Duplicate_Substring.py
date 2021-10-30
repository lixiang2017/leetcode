'''
Time Limit Exceeded
26 / 66 test cases passed.

Brute Force
T: O(N^2)
S: O(N^2)
'''
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        N = len(s)
        h = defaultdict(int)
        ans = ''
        for i in range(N):
            for j in range(i + 1, N + 1):
                h[s[i: j]] += 1
                if h[s[i: j]] > 1 and len(s[i: j]) > len(ans):
                    ans = s[i: j]
        return ans




'''
Rolling Hash
T: O(NlogN)
S: O(N)

Runtime: 1216 ms, faster than 91.05% of Python3 online submissions for Longest Duplicate Substring.
Memory Usage: 18.8 MB, less than 70.15% of Python3 online submissions for Longest Duplicate Substring.
'''
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        N = len(s)
        # convert string to array of integers 
        nums = [ord(s[i]) - ord('a') for i in range(N)]
        # base value for the rolling hash function
        b = 26
        # module value for the rolling hash function to avoid overflow
        # module = 10 ** 9 + 7  # wrong answer
        module = 10 ** 11 + 7
        
        # binary search, L = repeating string length
        l, r = 1, N
        while l != r:
            L = l + (r - l) // 2
            if self.search(L, b, module, N, nums) != -1:
                l = L + 1
            else:
                r = L
        
        start = self.search(l - 1, b, module, N, nums)
        return s[start: start + l - 1] if start != -1 else '' 
    
    
    def search(self, L: int, b: int, module: int, N: int, nums: List[int]) -> int:
        '''
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length that occurs at least 2 times.
        @return start position if the substring exists, -1 otherwise.
        '''
        # compute the hash of string s[: L]
        h = 0
        for i in range(L):
            h = (h * b + nums[i]) % module
        
        # already seen hashes of strings of length L
        seen = {h}
        # const value to be used often: b**L % module
        bL = pow(b, L, module)
        for start in range(1, N - L + 1):
            # compute rolling hash in O(1) time
            h = (h * b - nums[start - 1] * bL + nums[start + L - 1]) % module
            if h in seen:
                return start
            seen.add(h)
        return -1

