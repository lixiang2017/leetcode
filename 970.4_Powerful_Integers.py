'''
Author: lixiang
DFS Solution
Success
Details 
Runtime: 12 ms, faster than 99.63% of Python online submissions for Powerful Integers.
Memory Usage: 11.9 MB, less than 19.01% of Python online submissions for Powerful Integers.
'''

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        ans = set()
        
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            n = x ** i + y ** j
            if n <= bound:
                ans.add(n)
                if x > 1:
                    stack.append((i+1, j))
                if y > 1:
                    stack.append((i, j+1))

        ans = list(ans)
        return ans
        
if __name__ == "__main__":
    x = 2
    y = 3
    bound = 10
    assert Solution().powerfulIntegers(x, y, bound) == [2, 3, 4, 5, 7, 9, 10]

    x = 3
    y = 5
    bound = 15
    assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 6, 8, 10, 14]

    x = 1
    y = 1
    bound = 5
    assert Solution().powerfulIntegers(x, y, bound) == [2]

    x = 40
    y = 50
    bound = 10000
    Solution().powerfulIntegers(x, y, bound) == [2, 41, 51, 90, 1601, 1650, 2501, 2540, 4100]

    x = 2
    y = 1
    bound = 10
    print Solution().powerfulIntegers(x, y, bound) # [9, 2, 3, 5] # The result is not sorted.
    # [2, 3, 5, 9]

    x = 1
    y = 3
    bound = 20
    assert Solution().powerfulIntegers(x, y, bound) == [2, 4, 10]
