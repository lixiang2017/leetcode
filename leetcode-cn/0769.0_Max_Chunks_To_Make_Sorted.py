'''
semi - brute force
T: O(N^2 * logN)
S: O(N)

执行用时：36 ms, 在所有 Python3 提交中击败了68.73% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了74.27% 的用户
通过测试用例：52 / 52
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

执行用时：36 ms, 在所有 Python3 提交中击败了68.73% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了79.48% 的用户
通过测试用例：52 / 52
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
del diff[a]

执行用时：32 ms, 在所有 Python3 提交中击败了88.60% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了5.21% 的用户
通过测试用例：52 / 52
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
        

