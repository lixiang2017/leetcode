'''
Sort + DP,T:O(NlogN),S:O(1)
49 / 49 个通过测试用例
状态：通过
执行用时: 104 ms
内存消耗: 21.5 MB
提交时间：10 小时前
'''
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        return arr[-1]




'''
执行用时：96 ms, 在所有 Python3 提交中击败了85.92% 的用户
内存消耗：22.3 MB, 在所有 Python3 提交中击败了17.51% 的用户
'''
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        return reduce(lambda x, y: min(x + 1, y), sorted([0] + arr))

'''
Count/Hash Table,T:O(N),S:O(N)
执行用时：168 ms, 在所有 Python3 提交中击败了9.46% 的用户
内存消耗：33.1 MB, 在所有 Python3 提交中击败了5.23% 的用户
'''
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        cnt = defaultdict(int)
        for num in arr:
            cnt[min(num, N)] += 1
        miss = 0
        for i in range(1, N + 1):
            if cnt[i] == 0:
                miss += 1
            else:
                miss -= min(cnt[i] - 1, miss)
                # miss -= cnt[i] - 1  # wrong

        return N - miss
