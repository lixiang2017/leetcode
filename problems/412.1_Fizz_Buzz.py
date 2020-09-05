'''
Author: lixiang
Success
Details 
Runtime: 32 ms, faster than 65.25% of Python online submissions for Fizz Buzz.
Memory Usage: 12.7 MB, less than 34.60% of Python online submissions for Fizz Buzz.
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (not i  % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


if __name__ == '__main__':
    n = 15
    result = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
    assert Solution().fizzBuzz(n) == result