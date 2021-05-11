'''
appproach: Hash Table
Time: O(N + N + N) = O(N)
Space: O(N)

You are here!
Your runtime beats 52.63 % of python submissions.
You are here!
Your memory usage beats 44.53 % of python submissions.
'''


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
            
        error = []
        for i in range(1, N + 1):                
            if i in seen and seen[i] > 1:
                error.append(i)   
                
        for i in range(1, N + 1):
            if i not in seen:
                error.append(i)        
        return error


'''
approach: Set
Time: O(N + N + N) = O(N)
Space: O(N)

You are here!
Your runtime beats 95.55 % of python submissions.
You are here!
Your memory usage beats 44.53 % of python submissions.
'''

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        total = sum(nums)
        right = N * (1 + N) / 2
        distinct = sum(set(nums))
        repitition = total - distinct
        return [repitition, right - distinct]

