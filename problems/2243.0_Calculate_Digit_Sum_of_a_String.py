'''
simulation
T: O(k(s-k)/(k-1)) 等比数列求和
S: O(len(s))

Runtime: 51 ms, faster than 43.04% of Python3 online submissions for Calculate Digit Sum of a String.
Memory Usage: 13.9 MB, less than 17.24% of Python3 online submissions for Calculate Digit Sum of a String.
'''
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        ss = list(s)
        while len(ss) > k:
            ds = []
            for i in range(0, len(ss), k):
                t = 0
                for j in range(i, i + k):
                    if j < len(ss):
                        t += int(ss[j])
                ds += list(str(t))
            ss = ds 
        return ''.join(ss)
        
