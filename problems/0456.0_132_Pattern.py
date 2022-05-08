'''
Runtime: 5659 ms, faster than 5.12% of Python3 online submissions for 132 Pattern.
Memory Usage: 32.3 MB, less than 12.38% of Python3 online submissions for 132 Pattern.
'''
'''
nums[i]
left_min[i] = min(nums[: i])
right_part = sorted(nums[i + 1])
binary search right_part to find left_min[i] < x < nums[i]

'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        left_min = [float('inf')] * n
        right_part = []
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i - 1])
        
        for i in range(n - 2, -1, -1):
            bisect.insort(right_part, nums[i + 1])
            l = bisect_right(right_part, left_min[i])
            if l < len(right_part) and left_min[i] < right_part[l] < nums[i]:
                return True
        
        return False 
        
        
        
'''
Runtime: 596 ms, faster than 20.96% of Python3 online submissions for 132 Pattern.
Memory Usage: 32.1 MB, less than 33.50% of Python3 online submissions for 132 Pattern.
'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        left_min = [float('inf')] * n
        right_part = []
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i - 1])
            
        stack = [nums[-1]] 
        for i in range(n - 2, -1, -1):
            if nums[i] > left_min[i]:
                # from left to right, left_min descreasing
                # so we can pop stack, to remove no use data
                while stack and stack[-1] <= left_min[i]:
                    stack.pop()
                # no need to check stack[-1] > left_min[i] 
                if stack and stack[-1] < nums[i]:
                    return True
            # seen before, to record
            stack.append(nums[i])
        return False 
        

'''
Runtime: 348 ms, faster than 95.38% of Python3 online submissions for 132 Pattern.
Memory Usage: 32.1 MB, less than 67.82% of Python3 online submissions for 132 Pattern.
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n, stack = len(nums), []
        s2 = float('-inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < s2:
                return True
            while stack and nums[i] > stack[-1]:
                s2 = stack.pop()
            stack.append(nums[i])
            
        return False
            

            
        
