'''
hash table

执行用时：180 ms, 在所有 Python3 提交中击败了15.66% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了49.40% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        id2times = defaultdict(set)
        for id, time in logs:
            id2times[id].add(time)
        freq = Counter(len(v) for v in id2times.values())
        return [freq[i] for i in range(1, k + 1)]

'''
hash table

执行用时：100 ms, 在所有 Python3 提交中击败了84.34% 的用户
内存消耗：20.9 MB, 在所有 Python3 提交中击败了36.15% 的用户
通过测试用例：38 / 38
'''
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        id2times = defaultdict(set)
        for id, time in logs:
            id2times[id].add(time)
        ans = [0] * k
        for id, times in id2times.items():
            ans[len(times) - 1] += 1
        return ans 

