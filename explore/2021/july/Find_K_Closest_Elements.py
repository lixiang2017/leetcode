'''
approach: Binary Search + Two Pointers
Time: O(logN + k)
Space: O(1)

You are here!
Your runtime beats 67.96 % of python3 submissions.
You are here!
Your memory usage beats 69.77 % of python3 submissions.
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        l, r = 0, N - 1
        closest = 0
        
        while l <= r:
            mid = (r - l) // 2 + l
            if arr[mid] == x:
                closest = mid
                break
            elif arr[mid] > x:
                r = mid - 1
                closest = mid - 1
            else:
                l = mid + 1
                closest = mid + 1
        
        if closest <= 0:
            return arr[:k]
        if closest >= N - 1:
            return arr[-k:]
        
        bak = closest
        if abs(arr[closest + 1] -x) < abs(arr[closest] -x):
            closest += 1
        if abs(arr[bak - 1] -x) < abs(arr[bak] -x):
            closest = bak - 1
        i = j = closest
        min_diff = abs(arr[i] - x)
        while j - i + 1 < k:
            if 0 == i:
                return arr[:k]
            if N - 1 == j:
                return arr[-k:]
            
            if i - 1 >= 0 and j + 1 < N:
                if abs(arr[i - 1] - x) <= abs(arr[j + 1] - x):
                    i -= 1
                else:
                    j += 1
            elif i - 1 < 0:
                 return arr[:k]
            else:
                return arr[-k:]
        
        return arr[i: j + 1]
        


'''
approach: Binary Search
Time: O(logN)
Space: O(1)

You are here!
Your runtime beats 90.93 % of python3 submissions.
You are here!
Your memory usage beats 40.37 % of python3 submissions.
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr) - k
        while low < high:
            mid = (low + high) // 2
            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid
            
        return arr[low: low + k]
