'''
Hash Set
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 19.03 % of python3 submissions.
You are here!
Your memory usage beats 40.71 % of python3 submissions.
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        N = len(nums)
        seen = [False] * N
        ans = 0
        nested = set()
        elements = set(list(range(N)))
        while elements:
            one = elements.pop()  
            while not seen[one]:
                nested.add(one)
                elements.discard(one)
                seen[one] = True
                one = nums[one]
            ans = max(ans, len(nested))
            nested.clear()
        
        return ans

'''
nested可以不用set

You are here!
Your runtime beats 19.03 % of python3 submissions.
You are here!
Your memory usage beats 27.21 % of python3 submissions.
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        N = len(nums)
        seen = [False] * N
        ans = 0
        nested = 0
        elements = set(list(range(N)))
        while elements:
            one = elements.pop()    
            while not seen[one]:
                nested +=1 
                elements.discard(one)
                seen[one] = True
                one = nums[one]
            ans = max(ans, nested)
            nested = 0
        return ans


'''
T: O(N)
S: O(1)

You are here!
Your runtime beats 32.74 % of python3 submissions.
You are here!
Your memory usage beats 88.05 % of python3 submissions.
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        MAX = 10 ** 6
        for i in range(N):
            if nums[i] == MAX:
                continue
            nested = 0
            while nums[i] != MAX:
                nested += 1
                j = nums[i]
                nums[i] = MAX
                i = j
            ans = max(ans, nested)
            nested = 0
        return ans





