'''
semi - brute force
T: O(N^2 * logN)
S: O(N)

执行用时：1232 ms, 在所有 Python3 提交中击败了5.23% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了31.98% 的用户
通过测试用例：139 / 139
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s = sorted(arr)
        ans = 0
        for i in range(1, len(arr) + 1):
            if sorted(arr[: i]) == s[: i]:
                ans += 1
        return ans 


'''
sort + hash table 
T: O(NlogN + N)
S: O(N)

执行用时：64 ms, 在所有 Python3 提交中击败了26.16% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了18.60% 的用户
通过测试用例：139 / 139
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        diff = Counter()
        for a, b in zip(arr, sorted(arr)):
            diff[a] += 1
            if diff[a] == 0:
                del diff[a]
            diff[b] -= 1
            if diff[b] == 0:
                del diff[b]
            if len(diff) == 0:
                ans += 1
        return ans 

'''
diff.pop(a)

执行用时：76 ms, 在所有 Python3 提交中击败了22.67% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.81% 的用户
通过测试用例：139 / 139
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        diff = Counter()
        for a, b in zip(arr, sorted(arr)):
            diff[a] += 1
            if diff[a] == 0:
                diff.pop(a)
            diff[b] -= 1
            if diff[b] == 0:
                diff.pop(b)
            if len(diff) == 0:
                ans += 1
        return ans 


'''
用两个长度n的数组。
    leftMax[i] 表示 arr[0] ~ arr[i] 的最大值
    rightMin[i] 表示 arr[i]~arr[n - 1] 的最小值
那么，对于 1~(n -1) 的每一个i，只要 leftMax[i - 1] <= rightMin[i] 那么就可以在 i - 1 和 i 之间切断。
复杂度 O(N)


执行用时：48 ms, 在所有 Python3 提交中击败了54.07% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了39.53% 的用户
通过测试用例：139 / 139
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        # left max, right max 
        left, right = [arr[0]] * n, [arr[-1]] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], arr[i])
            if left[i] <= right[i + 1]:
                ans += 1
        return ans + 1 

'''
执行用时：52 ms, 在所有 Python3 提交中击败了43.60% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了28.49% 的用户
通过测试用例：139 / 139
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        # left max, right max 
        left, right = [arr[0]] * n, [arr[-1]] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], arr[i])
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], arr[i])
        return sum(left[i] <= right[i + 1] for i in range(n - 1)) + 1









