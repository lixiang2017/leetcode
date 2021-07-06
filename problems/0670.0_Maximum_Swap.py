'''
approach: Sort + Two Pointers
Time: O(NlogN + N) = O(NlogN), which N is the length of the given num.
Space: O(2N) = O(N)

Runtime: 32 ms, faster than 55.20% of Python3 online submissions for Maximum Swap.
Memory Usage: 14.2 MB, less than 79.97% of Python3 online submissions for Maximum Swap.
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        digits_sorted = sorted(digits, reverse=True)
        max_most = int(''.join(digits_sorted))
        if max_most == num:
            return num
        
        N = len(digits)
        i = 0
        while i < N:
            if digits[i] != digits_sorted[i]:
                break
            i += 1
        
        j = N - 1
        while j > i and digits_sorted[i] != digits[j]:
            j -= 1
        
        digits[i], digits[j] = digits[j], digits[i]
        return int(''.join(digits))
            
        