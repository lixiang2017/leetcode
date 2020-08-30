'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/552/week-4-august-22nd-august-28th/3439/
You are here!
Your runtime beats 92.65 % of python submissions.

https://en.wikipedia.org/wiki/Expected_value
https://en.wikipedia.org/wiki/Rejection_sampling
'''

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1




# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        return random.randint(1, 10)




'''
You are here!
Your runtime beats 66.18 % of python submissions.
You are here!
Your memory usage beats 17.65 % of python submissions.
'''

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            x = (a - 1) * 7 + b     # rand49()
            if x <= 40:             # [1, 40]
                return x % 10 + 1
        
            a = x - 40              # [1, 9]  rand9()
            b = rand7()
            x = (a - 1) * 7 + b     # [1, 63] rand63()
            if x <= 60:
                return x % 10 + 1
            
            a = x - 60              # [1, 3]  rand3()
            b = rand7()
            x = (a - 1) * 7 + b     # [1, 21] rand21()
            if x <= 20:
                return x % 10 + 1
        