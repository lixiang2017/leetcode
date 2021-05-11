'''
approach: Three Pointers
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 10.69 % of python3 submissions.
You are here!
Your memory usage beats 74.34 % of python3 submissions.
'''


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        sub = 0
        i, N = 0, len(s)
        while i + 1 < N:
            if s[i] != s[i + 1]:
                # j to left, k to right
                j, k = i, i + 1
                while j >= 0 and k < N:
                    if s[j] == s[i] and s[k] == s[i + 1]:
                        sub += 1
                        j -= 1
                        k += 1
                    else:
                        break
                i = k - 1
            else:
                i += 1
        
        return sub


'''
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 80.81 % of python3 submissions
You are here!
Your memory usage beats 43.11 % of python3 submissions.
'''
from itertools import groupby

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        lens = [len(list(group)) for key, group in groupby(s)]
        return sum(min(a, b) for a, b in zip(lens, lens[1: ]))

'''
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 33.93 % of python3 submissions.
You are here!
Your memory usage beats 74.34 % of python3 submissions.
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans

'''
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 53.69 % of python3 submission
You are here!
Your memory usage beats 43.11 % of python3 submissions.
'''

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N, ptr, last, ans = len(s), 0, 0, 0
        while ptr < N:
            ch = s[ptr]
            count = 0
            while ptr < N and s[ptr] == ch:
                count += 1
                ptr += 1
            ans += min(last, count)
            last = count
            
        return ans
    