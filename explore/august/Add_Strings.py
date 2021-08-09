'''
You are here!
Your runtime beats 97.02 % of python3 submissions.
You are here!
Your memory usage beats 64.61 % of python3 submissions.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))

'''
Simulation
类似两个链表求和

You are here!
Your runtime beats 57.07 % of python3 submissions.
You are here!
Your memory usage beats 40.18 % of python3 submissions.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        M, N = len(num1), len(num2)
        carry, i, j = 0, M - 1, N - 1
        digit = 0
        while i >= 0 and j >= 0:
            total = ord(num1[i]) - ord('0') + ord(num2[j]) - ord('0') + carry
            if total > 9:
                digit = total - 10
                carry = 1
            else:
                digit = total
                carry = 0
                
            ans.append(str(digit))
            i -= 1
            j -= 1
    
        while i >= 0:
            total = ord(num1[i]) - ord('0') + carry
            if total > 9:
                digit = total - 10
                carry = 1
            else:
                digit = total
                carry = 0
            ans.append(str(digit))
            i -= 1

        while j >= 0:
            total = ord(num2[j]) - ord('0') + carry
            if total > 9:
                digit = total - 10
                carry = 1
            else:
                digit = total
                carry = 0
                
            ans.append(str(digit))
            j -= 1
        
        if carry:
            ans.append('1')
            
        return "".join(ans[:: -1]) if ans else '0'
        

'''
其实不用分三种情况。或者即可。

You are here!
Your runtime beats 71.10 % of python3 submissions.
You are here!
Your memory usage beats 21.05 % of python3 submissions.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        M, N = len(num1), len(num2)
        carry, i, j = 0, M - 1, N - 1
        digit = 0
        while i >= 0 or j >= 0 or carry:
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0
            total =  x + y + carry
            if total > 9:
                digit = total - 10
                carry = 1
            else:
                digit = total
                carry = 0
                
            ans.append(str(digit))
            i -= 1
            j -= 1
    
        return "".join(ans[:: -1]) if ans else '0'
        


