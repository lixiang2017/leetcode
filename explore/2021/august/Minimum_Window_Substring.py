'''
Hash Table + Sliding Window

You are here!
Your runtime beats 14.43 % of python3 submissions.
You are here!
Your memory usage beats 29.51 % of python3 submissions.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        ans = ''
        min_len = float('inf')
        l, r = 0, 0
        need = Counter(t)
        curr = defaultdict(int)
        
        def check(curr, need):
            for key in need.keys():
                if curr[key] < need[key]:
                    return False
            return True
        
        while l < N and r < N:
            # right side move forward
            while r < N:
                curr[s[r]] += 1
                r += 1
                if check(curr, need):
                    if 0 < r - l < min_len:
                        min_len = r - l
                        ans = s[l: r]  
                    break
                else:
                    continue

            # left side move forward
            while l < r:
                curr[s[l]] -= 1
                l += 1
                if check(curr, need):
                    if 0 < r - l < min_len:
                        min_len = r - l
                        ans = s[l: r]  
                else:
                    break
                    
        return ans



'''
"ADOBECODEBANC"
"ABC"
"a"
"a"
"a"
"aa"
"ab"
"a"
"ab"
"A"
'bba'
'ab'
"cabefgecdaecf"
"cae"

Input: "ab"
"a"
Output: ""
Expected: "a"

Input: "ab"
"A"
Output: "b"
Expected: ""

Input: "bba"
"ab"
Output: "bba"
Expected: "ba"

Input: "cabefgecdaecf"
"cae"
Output: "cabe"
Expected: "aec"

Input: "acbbaca"
"aba"
Output: ""
Expected: "baca"
'''


