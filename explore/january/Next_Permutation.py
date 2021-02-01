'''
Time: O(N + N + N) = O(N)
Space: O(1)

Intuitive: the tail part will be in decreasing order
Solution:
1. find the stop_idx, which is not decreased.
2. find the first number greater than the top number, keep greater_idx
3. swap the stop number and the first greater number
4. reverse the tail

You are here!
Your runtime beats 19.23 % of python submissions.
You are here!
Your memory usage beats 75.65 % of python submissions.

example:
3 1 5 4 2 -> 3 2 1 4 5
1 2 5 4 3 -> 1 3 2 4 5
2 1 5 4 3 -> 2 3 1 4 5
5 4 3 2 1 -> 1 2 3 4 5
4 1 5 3 2 -> 4 2 1 3 5
4 5 3 2 1 -> 5 1 2 3 4
1 2 3 4 5 -> 1 2 3 5 4
1 -> 1
5 -> 5
1 1 5 -> 1 5 1
2 2 2 2 5 -> 2 2 2 5 2
3 3 3 5 3 -> 3 3 5 3 3
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size == 1: return None
        
        stop_idx = - 1
        for i in range(size - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                stop_idx = i - 1
                break
        # print 'stop_idx: ', stop_idx   
        if stop_idx == -1:
            # nums = nums[:: -1]  # wrong answer
            nums.reverse()
            # print 'nums: ', nums
            return None
        
        greater_idx = -1
        for i in range(size - 1, stop_idx, -1):
            if nums[i] > nums[stop_idx]:
                greater_idx = i
                break
        # swap       
        nums[stop_idx], nums[greater_idx] = nums[greater_idx], nums[stop_idx]
        # reverse tail
        left, right = stop_idx + 1, size - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        # combine
        # print 'tail: ', nums[stop_idx + 1:][:: -1]
        # nums = nums[: stop_idx + 1] + nums[stop_idx + 1:][:: -1]  # wrong answer
        # print 'nums 9: ', nums

'''
Wrong Answer 
Input:
[3,2,1]
Output:
[3,2,1]
Expected:
[1,2,3]   

Wrong Answer 
Input:
[1,3,2]
Output:
[2,3,1]
Expected:
[2,1,3]
'''

