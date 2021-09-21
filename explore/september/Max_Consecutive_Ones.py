'''
T: O(N)
S: O(1)

You are here!
Your runtime beats 51.96 % of python3 submissions.
You are here!
Your memory usage beats 48.55 % of python3 submissions.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = curr = 0
        for x in nums:
            if 0 == x:
                curr = 0
            else:
                curr += 1
                m = max(m, curr)
        return m

'''
You are here!
Your runtime beats 63.20 % of python3 submissions.
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split('0') ))
