'''
Time: O(N)
Space: O(N)

You are here!
Your runtime beats 21.99 % of python submissions.
You are here!
Your memory usage beats 13.77 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values == values[:: -1]
