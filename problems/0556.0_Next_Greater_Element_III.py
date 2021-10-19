'''
Greedy

Runtime: 37 ms, faster than 36.18% of Python3 online submissions for Next Greater Element III.
Memory Usage: 14.4 MB, less than 23.98% of Python3 online submissions for Next Greater Element III.
'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        if digits == sorted(digits, reverse=True):
            return -1
        L = len(digits)
        pl = L - 1  # peak left index
        for i in range(L - 1, -1, -1):
            if digits[i] > digits[i - 1]:
                pl = i - 1
                break
        cand = L - 1  # candidate index
        for i in range(L - 1, pl, -1):
            if digits[i] > digits[pl]:
                cand = i
                break
        ans = ''.join(digits[: pl] + [digits[cand]] + sorted(digits[pl: cand] + digits[cand + 1: ]))    
        ans = int(ans)
        return [-1, ans][ans <= (1 << 31) - 1]
        