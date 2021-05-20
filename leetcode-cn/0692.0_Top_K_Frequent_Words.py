'''
Counter + Sort, T:O(N + N + NlogN + N)=O(NlogN),S:O(N)

执行用时：52 ms, 在所有 Python3 提交中击败了99.92% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.46% 的用户
'''

from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        freq = [(word, times) for word, times in freq.items()]
        freq.sort(key=lambda k: (-k[1], k[0]))
        return [word for word, _ in freq[: k]]



'''
Heap
Time: O(NlogK)
Space: O(N)

执行用时：60 ms, 在所有 Python3 提交中击败了95.34% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了59.33% 的用户
'''


from collections import Counter
import heapq

class Cmp:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word      # !!!

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        q = []
        for word, times in freq.items():
            if len(q) < k:
                heapq.heappush(q, Cmp(times, word))
            elif (times > q[0].freq or (times == q[0].freq and word < q[0].word)):
                heapq.heapreplace(q, Cmp(times, word))

        return [heapq.heappop(q).word for _ in range(k)][:: -1]

'''
["i", "love", "leetcode", "i", "love", "coding"]
2
["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
4
["i", "love", "leetcode", "i", "love", "coding"]
3
'''