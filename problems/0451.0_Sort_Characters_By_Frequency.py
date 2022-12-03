'''
Runtime: 36 ms, faster than 93.60% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 15.6 MB, less than 41.52% of Python3 online submissions for Sort Characters By Frequency.
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sf = sorted([(c, k) for k, c in freq.items()], reverse=True)
        return ''.join(k * c for c, k in sf)

'''
Runtime: 349 ms, faster than 5.07% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 28.4 MB, less than 5.07% of Python3 online submissions for Sort Characters By Frequency.
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ss = sorted(s, key=lambda ch: (-cnt[ch], ch))
        return ''.join(ss)
        