'''
Python3
44 ms
16.1 MB
'''
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range((n + 1) // 2):
            if i == n - 1 - i:
                ans += nums[i]
            else:
                a, b = nums[i], nums[n - 1 - i]
                ans += int(str(a) + str(b))
        return ans 
    

'''
Python3
48 ms
16 MB
'''
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range((n + 1) // 2):
            if i == n - 1 - i:
                ans += nums[i]
            else:
                a, b = nums[i], nums[n - 1 - i]
                ans += a * 10 ** self.digit(b) + b 
        return ans 
    
    def digit(self, x: int) -> int:
        c = 0
        while x:
            x //= 10
            c += 1
        return c

