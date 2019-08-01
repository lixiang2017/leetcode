'''
Author: lixiang
Success
Details 
Runtime: 20 ms, faster than 99.68% of Python online submissions for Fizz Buzz.
Memory Usage: 12.7 MB, less than 36.49% of Python online submissions for Fizz Buzz.
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1, n+1)]


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