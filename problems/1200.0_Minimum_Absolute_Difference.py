'''
Runtime: 356 ms, faster than 52.64% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 28.1 MB, less than 84.81% of Python3 online submissions for Minimum Absolute Difference.
'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        diff = arr[1] - arr[0]
        for i in range(2, n):
            diff = min(diff, arr[i] - arr[i - 1])
        ans = []
        for i in range(1, n):
            if diff == arr[i] - arr[i - 1]:
                ans.append([arr[i - 1], arr[i]])
        return ans
        