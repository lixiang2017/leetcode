class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digitSum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        return min(digitSum(x) for x in nums)


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digitSum(x: int) -> int:
            s = 0
            while x:
                x, r = divmod(x, 10)
                s += r
            return s

        return min(digitSum(x) for x in nums)


class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = inf
        for x in nums:
            s = 0
            while x:
                s += x % 10
                if s >= ans:
                    break
                x //= 10
            ans = min(ans, s)
        return ans