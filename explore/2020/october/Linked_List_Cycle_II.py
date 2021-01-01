'''
You are here!
Your runtime beats 55.03 % of python submissions.
'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = pointer = head
        index = 0
        while slow and slow.next and fast and fast.next and fast.next.next:  #!!!
            slow = slow.next
            # if fast.next:   # AttributeError: 'NoneType' object has no attribute 'next'
            if fast and fast.next:
                fast = fast.next.next
            index += 1
            if slow == fast:
                print 'fast and slow meet at ', index

                step = 0
                new_pointer = head
                while (new_pointer != slow):
                    new_pointer = new_pointer.next
                    slow = slow.next
                    step += 1
                print 'tail connects to node index ', step
                return new_pointer
                break
        
        print 'no cycle'
        return None
    