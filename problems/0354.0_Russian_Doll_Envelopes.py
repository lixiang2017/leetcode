'''
sort + dp

82 / 87 test cases passed.
    Status: Time Limit Exceeded

T: O(NlogN + N^2)
S: O(N)
'''
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        dp = [1] * n 
        for i in range(1, n):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


'''
LIS
sort + binary search
T: O(NlogN + NlogN)
S: O(N)

Runtime: 1665 ms, faster than 48.70% of Python3 online submissions for Russian Doll Envelopes.
Memory Usage: 61.9 MB, less than 21.58% of Python3 online submissions for Russian Doll Envelopes.
'''
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        f = [envelopes[0][1]]
        for i in range(1, n):
            h = envelopes[i][1]
            if h > f[-1]:
                f.append(h)
            else:
                idx = bisect_left(f, h)
                f[idx] = h 
        return len(f)
