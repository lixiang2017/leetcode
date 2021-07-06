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
