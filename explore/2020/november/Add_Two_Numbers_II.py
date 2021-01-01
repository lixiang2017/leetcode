'''
1563 / 1563 test cases passed.
Status: Accepted
Runtime: 112 ms
Memory Usage: 13.5 MB
Submitted: 1 minute ago
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # to store the first and second number
        # first = second = []  # Wrong ! first:  [7, 2, 4, 3, 5, 6, 4]   second:  [7, 2, 4, 3, 5, 6, 4]
        first = []
        second = []
        while l1:
            first.append(l1.val)
            l1 = l1.next
        while l2:
            second.append(l2.val)
            l2 = l2.next
        print 'first: ', first
        print 'second: ', second
        
        # on the fly
        prev = None
        carry = 0
        while True:
            if len(first) > 0:
                one = first.pop()
            else:
                one = 0     
            if len(second) > 0:
                another = second.pop()
            else:
                another = 0
            digits_sum = carry + one + another
            print 'digits_sum: ', digits_sum
            
            # if digits_sum == 0:   # will be Wrong answer
            if digits_sum == 0 and len(first) == 0 and len(second) == 0:
                break  
            elif digits_sum > 9:
                carry = 1
                digits_sum -= 10
            else:
                carry = 0    # very important!
            prev = ListNode(digits_sum, prev)
        
        # return prev
        return prev if prev else ListNode(0) 

'''
Submission Result: Wrong Answer 
Input:
[0]
[0]
Output:
[]
Expected:
[0]
Stdout:
first:  [0]
second:  [0]
digits_sum:  0
'''

'''
Input:
[6,4,5,0,4,4,9,4,1]
[3,8,8,0,3,0,1,4,8]
Output:
[7,5,0,8,9]
Expected:
[1,0,3,3,0,7,5,0,8,9]
Stdout:
first:  [6, 4, 5, 0, 4, 4, 9, 4, 1]
second:  [3, 8, 8, 0, 3, 0, 1, 4, 8]
digits_sum:  9
digits_sum:  8
digits_sum:  10
digits_sum:  5
digits_sum:  7
digits_sum:  0
'''


