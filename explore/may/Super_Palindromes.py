'''
39 / 49 test cases passed.
Status: Time Limit Exceeded
Submitted: 0 minutes ago
Last executed input:
"43143"
"7072263972576"
'''

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        start, end = int(left ** 0.5), int(right ** 0.5)
        if start * start != left:
            start += 1
        cnt = 0
        for i in range(start, end + 1):
            if str(i) == str(i)[:: -1] and str(i * i) == str(i * i)[:: -1]:
                cnt += 1
        
        return cnt



'''
approach: mathematical
Time: O(W^(1/4) * logW)
Space: O(logW)

You are here!
Your memory usage beats 43.59 % of python3 submissions.
'''

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        MAGIC = 100000
        
        def reverse(x):
            ans = 0
            while x:
                ans = ans * 10 + x % 10
                x //= 10     # !!!!    /= will be wrong! Python3(//) Python2(/)
            return ans
        
        def is_palindrome(x):
            return x == reverse(x)
        
        ans = 0
        # count odd length 
        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and is_palindrome(v):
                ans += 1
        
        # count even length
        for k in range(MAGIC):
            s = str(k)
            t = s + s[:: -1]
            v = int(t) ** 2
            if v > right:
                break
            if v >= left and is_palindrome(v):
                ans += 1
        
        return ans
    
    
'''
"4"
"1000"
"1"
"2"
"43143"
"7072263972576"
'''
    

