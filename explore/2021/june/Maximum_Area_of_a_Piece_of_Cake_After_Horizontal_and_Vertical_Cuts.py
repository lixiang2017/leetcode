'''
approach: Sort + Max Diff
Time: O(MlogM + NlogN)
Space: O(1)

You are here!
Your memory usage beats 22.53 % of python3 submissions.
'''

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        MOD = 10 ** 9 + 7
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        max_h_diff = max_v_diff = 0
        H, V = len(horizontalCuts), len(verticalCuts)
        for i in range(H - 1):
            max_h_diff = max(max_h_diff, horizontalCuts[i + 1] - horizontalCuts[i])
            max_h_diff %= MOD
        for j in range(V - 1):
            max_v_diff = max(max_v_diff, verticalCuts[j + 1] - verticalCuts[j])
            max_v_diff %= MOD
        
        return max_h_diff * max_v_diff % MOD
