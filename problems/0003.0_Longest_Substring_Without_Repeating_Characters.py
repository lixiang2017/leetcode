'''
two pointers / sliding window

T: O(N)
S: O(26 + 26 + 10 + 1) = O(1)

Runtime: 112 ms, faster than 38.09% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 49.19% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        ans = 0
        i = j = 0
        while j < n:
            if s[j] not in seen:
                seen.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            else:
                while i < j and s[j] in seen:
                    seen.remove(s[i])
                    i += 1
        return ans 


'''
no use for i < j

Runtime: 100 ms, faster than 46.88% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.1 MB, less than 49.19% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        ans = 0
        i = j = 0
        while j < n:
            if s[j] not in seen:
                seen.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
        return ans 


'''
just one while 

Runtime: 66 ms, faster than 85.44% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14 MB, less than 93.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        n = len(s)
        ans = 0
        i = j = 0
        while j < n:
            if s[j] not in seen:
                seen.add(s[j])
                ans = max(ans, j - i + 1)
                j += 1
            else:
                seen.remove(s[i])
                i += 1
        return ans 


