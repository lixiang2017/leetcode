class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev = '#'
        zero = one = 0
        for ch in s:
            if ch == prev:
                if ch == '0':
                    zero += 1
                else:
                    one += 1
            else:
                if ch == '0':
                    # prev = '1'
                    ans += min(zero, one)
                    zero = 1
                else: # ch == '1'
                    # prev = '0'
                    ans += min(zero, one)
                    one = 1
            prev = ch 
        return ans + min(zero, one)


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counts = []
        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            count = 0
            while i < n and s[i] == ch:
                i += 1
                count += 1
            counts.append(count)

        ans = 0
        for c0, c1 in pairwise(counts):
            ans += min(c0, c1)
        return ans


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = last = ans = 0
        n = len(s)
        while i < n:
            count = 0
            ch = s[i]
            while i < n and s[i] == ch:
                count += 1
                i += 1
            ans += min(last, count)
            last = count
        return ans 
