'''
approach: Sort + Dynamic Programming
Time: O(NlogN + N^2 + N) = O(N^2)
Space: O(N)

执行用时：7440 ms, 在所有 Python 提交中击败了34.84%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # envelopes = sorted(envelopes, key=lambda env: (env[0], -env[1]))
        envelopes.sort(key=lambda env: (env[0], -env[1]))
        N = len(envelopes)
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)



'''
approach: Sort + Greedy + Binary Search
Time: O(NlogN + NlogN) = O(NlogN)
Space: O(N)

执行用时：60 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了100.00%的用户
'''

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda env: (env[0], -env[1]))
        N = len(envelopes)
        d = []
        for w, h in envelopes:
            if not d or h > d[-1]:
                d.append(h)
            else:
                left, right = 0, len(d) - 1
                loc = right
                while left <= right:
                    mid = (left + right) / 2
                    if d[mid] >= h:
                        loc = mid 
                        right = mid - 1
                    else:
                        left = mid + 1
                d[loc] = h
        return len(d)
