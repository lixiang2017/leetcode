'''
T: O(2N)
S: O(60) = O(1)

Runtime: 232 ms, faster than 66.00% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
Memory Usage: 17.6 MB, less than 79.38% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        rem = [t % 60 for t in time]
        c = defaultdict(int)
        p = 0
        for r in rem:
            p += c[60 - r]
            c[r] += 1
        p += c[0] * (c[0] - 1) // 2
        return p

'''
T: O(N)
S: O(60) = O(1)

Runtime: 243 ms, faster than 39.62% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
Memory Usage: 17.8 MB, less than 63.65% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = [0] * 61
        p = 0
        for t in time:
            t %= 60
            p += c[60 - t]
            c[t] += 1
        p += c[0] * (c[0] - 1) // 2
        return p
    