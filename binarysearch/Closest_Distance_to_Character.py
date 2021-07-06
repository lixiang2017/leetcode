'''
Three Pass

Time: O(3N) = O(N)
Space: O(N)

Your code took 615 milliseconds — faster than 7.59% in Python
'''

class Solution:
    def solve(self, s, c):
        prev_idx = -100005
        left = []
        for idx, ch in enumerate(s):
            if ch == c:
                prev_idx = idx
            left.append(prev_idx)
        
        right = []
        N = len(s)
        post_idx = 100005
        for i in range(N - 1, -1, -1):
            if s[i] == c:
                post_idx = i
            # right.insert(0, post_idx)  # TLE
            right.append(post_idx)
        
        return [min(abs(left[i] - i), abs(right[N - 1 - i] - i)) for i in range(N)]

'''
Only Two Pass, calculate ans on the second pass
Time: O(2N) = O(N)
Space: O(N)

Your code took 338 milliseconds — faster than 47.05% in Python
'''
class Solution:
    def solve(self, s, c):
        prev_idx = -100005
        left = []
        for idx, ch in enumerate(s):
            if ch == c:
                prev_idx = idx
            left.append(prev_idx)
        
        ans = []
        right = []
        N = len(s)
        post_idx = 100005
        for i in range(N - 1, -1, -1):
            if s[i] == c:
                post_idx = i
            # right.insert(0, post_idx)  # TLE
            # right.append(post_idx)
            ans.append(min(abs(left[i] - i), abs(post_idx - i)))
        
        return ans[:: -1]
        # return [min(abs(left[i] - i), abs(right[N - 1 - i] - i)) for i in range(N)]

