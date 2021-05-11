'''
approach: Prefix Sum + Postfix Sum + Two Pointers/Sliding Window
Time: O(N + N + k)
Space: O(2N)

You are here!
Your runtime beats 11.32 % of python3 submissions.
You are here!
Your memory usage beats 67.63 % of python3 submissions.
'''


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        presum, postsum = [0] * N, [0] * N
        # presum
        for i in range(N):
            if 0 == i:
                presum[i] = cardPoints[i]
            else:
                presum[i] = presum[i - 1] + cardPoints[i]
        # postsum
        for i in range(N - 1, -1, -1):
            if N - 1 == i:
                postsum[i] = cardPoints[i]
            else:
                postsum[i] = postsum[i + 1] + cardPoints[i]
        max_score = max(presum[k - 1], postsum[- k])
        for i in range(k - 1):
            max_score = max(max_score, presum[i] + postsum[-k + i+ 1])
        
        return max_score
        