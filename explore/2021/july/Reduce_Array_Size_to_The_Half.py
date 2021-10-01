'''
approach: Hash Table + Sort
Time: O(N + NlogN + N)
Space: O(N + N)

You are here!
Your runtime beats 46.93 % of python3 submissions.
You are here!
Your memory usage beats 19.55 % of python3 submissions.
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        freq = Counter(arr)
        cnts = sorted([(num, cnt) for num, cnt in freq.items()], key=lambda t: -t[1])
        total = least = 0
        for _, cnt in cnts:
            total += cnt
            least += 1
            if total >= N // 2:
                break
        return least


'''
You are here!
Your runtime beats 44.83 % of python3 submissions.
'''
from collections import Counter, OrderedDict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        freq = Counter(arr)
        ordered = OrderedDict(sorted(freq.items(), key=lambda x: -x[1]))
        total = least = 0
        for _, cnt in ordered.items():
            total += cnt
            least += 1
            if total >= N // 2:
                break
        return least


'''
You are here!
Your runtime beats 91.06 % of python3 submissions.
You are here!
Your memory usage beats 77.79 % of python3 submissions.
'''
from collections import Counter, OrderedDict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        freq = Counter(arr)
        times = sorted(freq.values(), key=lambda x: -x)
        total = least = 0
        for t in times:
            total += t
            least += 1
            if total >= N // 2:
                break
        return least


'''
You are here!
Your runtime beats 99.72 % of python3 submissions.
'''
from collections import Counter, OrderedDict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        freq = Counter(arr)
        # times = sorted(freq.values(), key=lambda x: -x)
        times = list(freq.values())
        times.sort(reverse=True)
        total = least = 0
        for t in times:
            total += t
            least += 1
            if total >= N // 2:
                break
        return least
        



     
