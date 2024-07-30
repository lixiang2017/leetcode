'''
57ms 击败8.51%
16.35MB 击败91.49%
'''

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, variable in enumerate(variables):
            a, b, c, m = variable
            x = pow(a, b, 10)
            y = pow(x, c, m)
            if y == target:
                ans.append(i)
        return ans

