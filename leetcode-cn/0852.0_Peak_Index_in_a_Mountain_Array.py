'''
T:O(N),S:O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了24.47% 的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了61.42% 的用户
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        for i in range(1, N):
            if arr[i] < arr[i - 1]:
                return i - 1


'''
T:O(logN);S:O(1)

执行用时：48 ms, 在所有 Python3 提交中击败了24.47% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了88.28% 的用户
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if 0 < mid + 1 < N:
                if arr[mid] < arr[mid + 1]:
                    l = mid + 1
                else:
                    r = mid
            else:
                mid = N - 2
        return l
