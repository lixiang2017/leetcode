'''
simulation

You are here!
Your runtime beats 50.56 % of python3 submissions.
You are here!
Your memory usage beats 73.23 % of python3 submissions.
'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = list(map(int, num1.strip('i').split('+')))
        real2, imaginary2 = list(map(int, num2.strip('i').split('+')))
        real = real1 * real2 - imaginary1 * imaginary2
        imaginary = real1 * imaginary2 + real2 * imaginary1
        return str(real) + '+' + str(imaginary) + 'i' 
        