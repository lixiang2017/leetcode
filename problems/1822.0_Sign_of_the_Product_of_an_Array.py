'''
approach: Map
Time: O(N)
Space: O(N)

Runtime: 60 ms, faster than 77.52% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 14.5 MB, less than 6.56% of Python3 online submissions for Sign of the Product of an Array.
'''

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        negative = sum(-1 for num in nums if num < 0)
        return -1 if negative % 2 else 1

'''
Runtime: 74 ms, faster than 6.38% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 16.5 MB, less than 7.53% of Python3 online submissions for Sign of the Product of an Array.
'''
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for x  in nums:
            if x < 0:
                p *= -1
            elif x == 0:
                return 0
        return p


'''
Runtime: 75 ms, faster than 6.23% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 16.5 MB, less than 5.32% of Python3 online submissions for Sign of the Product of an Array.
'''
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
            
        return reduce(operator.mul, map(signFunc, nums))


'''
Runtime: 65 ms, faster than 39.12% of Python3 online submissions for Sign of the Product of an Array.
Memory Usage: 16.5 MB, less than 5.32% of Python3 online submissions for Sign of the Product of an Array.
'''
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        signFunc = lambda x: 1 if x > 0 else -1 if x < 0 else 0
        return reduce(operator.mul, map(signFunc, nums))
          