'''
You are here!
Your runtime beats 90.94 % of python submissions.
'''


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # deq, size, ans = deque([0]), len(nums), []
        deq, size, ans = deque(), len(nums), []
        
        for i in range(size):
            # to keep the number of elements in deque is less than or equal to k
            while deq and deq[0] <= i - k:
                deq.popleft()
            
            # to keep in descreasing order
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()
            
            deq.append(i)
            
            ans.append(nums[deq[0]])
            # print 'deq: ', deq
            # print 'nums in deq: ', [nums[i] for i in deq]
        
        # print 'ans: ', ans
        return ans[k - 1: ]

    
'''
Your input
[1,3,-1,-3,5,3,6,7]
3
Your stdout
deq:  deque([0])
deq:  deque([1])
deq:  deque([1, 2])
deq:  deque([1, 2, 3])
deq:  deque([4])
deq:  deque([4, 5])
deq:  deque([6])
deq:  deque([7])
ans:  [1, 3, 3, 3, 5, 5, 6, 7]

Submission Result: Output Limit Exceeded 
'''




    
'''
Your input
[1,3,-1,5,-3,5,10,10,10,10,3,6,7]
3
Your stdout
nums in deq:  [1]
nums in deq:  [3]
nums in deq:  [3, -1]
nums in deq:  [5]
nums in deq:  [5, -3]
nums in deq:  [5]
nums in deq:  [10]
nums in deq:  [10]
nums in deq:  [10]
nums in deq:  [10]
nums in deq:  [10, 3]
nums in deq:  [10, 6]
nums in deq:  [7]
ans:  [1, 3, 3, 5, 5, 5, 10, 10, 10, 10, 10, 10, 7]
'''


'''
Your input
[1,3,-1,5,-3,5,10,10,10,10,3,6,7]
3
Your stdout
deq:  deque([0])
deq:  deque([1])
deq:  deque([1, 2])
deq:  deque([3])
deq:  deque([3, 4])
deq:  deque([5])
deq:  deque([6])
deq:  deque([7])
deq:  deque([8])
deq:  deque([9])
deq:  deque([9, 10])
deq:  deque([9, 11])
deq:  deque([12])
ans:  [1, 3, 3, 5, 5, 5, 10, 10, 10, 10, 10, 10, 7]

Your answer
[3,5,5,5,10,10,10,10,10,10,7]
Expected answer
[3,5,5,5,10,10,10,10,10,10,7]

'''


