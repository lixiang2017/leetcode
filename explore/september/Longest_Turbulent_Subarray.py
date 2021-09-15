'''
Time: O(N)
Space: O(1)

You are here!
Your runtime beats 94.49 % of python3 submissions.
You are here!
Your memory usage beats 70.87 % of python3 submissions.
'''
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        if N < 2:
            return N
        
        longest = long = 1
        # pre
        # arr[i - 1] < arr[i]    -1
        # arr[i - 1] > arr[i]    1
        # arr[i - 1] = arr[i]    0
        pre = -2
        for i in range(1, N):
            if arr[i - 1] < arr[i]:
                if pre == 1:
                    long += 1
                else:
                    long = 2
                pre = -1
            elif arr[i - 1] > arr[i]:
                if pre == -1:
                    long += 1
                else:
                    long = 2
                pre = 1
            else:
                long = 1
                pre = -2
            longest = max(longest, long)
            
        return longest
