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


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [j for j, (a, b, c, m) in enumerate(variables) if pow(pow(a, b, 10), c, m) == target]


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def pow_mod(x: int, y: int, mod: int) -> int:
            res = 1
            while y:
                if y & 1:
                    res = res * x % mod 
                x = x * x % mod 
                y >>= 1
            return res 

        return [j for j, (a, b, c, m) in enumerate(variables) if pow_mod(pow_mod(a, b, 10), c, m) == target]

