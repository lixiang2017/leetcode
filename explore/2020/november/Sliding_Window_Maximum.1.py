'''
decreasing deque
# keep elements of deque in descreasing order

You are here!
Your runtime beats 21.74 % of python submissions.

Time: O(n)
Space: O(k)
'''


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deq, size, ans = deque([0]), len(nums), []
        
        for i in range(size):
            while deq and deq[0] <= i - k:
                deq.popleft()
                
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            
            deq.append(i)
            
            ans.append(nums[deq[0]])
        
        return ans[k - 1: ]
            