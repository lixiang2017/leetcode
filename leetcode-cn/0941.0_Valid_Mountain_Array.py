'''
64ms 击败 35.95%使用 Python3 的用户
16.71MB 击败 46.17%使用 Python3 的用户
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        j = i
        while j + 1 < n and arr[j] > arr[j + 1]:
            j += 1
        return n >= 3 and i > 0 and j == n - 1 and j > i 


'''
56ms 击败 74.07%使用 Python3 的用户
16.80MB 击败 12.38%使用 Python3 的用户
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l, r = 0, len(arr) - 1
        while l < r and arr[l] < arr[l + 1]:
            l += 1
        while l < r and arr[r] < arr[r - 1]:
            r -= 1
        return l == r and l > 0 and r < len(arr) - 1
