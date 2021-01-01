'''
You are here!
Your runtime beats 97.55 % of python submissions.
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
        length1 = self.getLength(l1)
        length2 = self.getLength(l2)
        if length1 > length2:
            #
            n = length1 - length2 - 1
            pointer = self.getIthPointer(l1, n)
            if 1 == self.sumLists(pointer.next, l2):
                if 1 == self.incrementDigit(l1, pointer):
                    head = ListNode(1, l1)
                    return head
            return l1
            
        elif length1 < length2:
            #
            n = length2 - length1 - 1
            pointer = self.getIthPointer(l2, n)
            if 1 == self.sumLists(pointer.next, l1):
                if 1 == self.incrementDigit(l2, pointer):
                    head = ListNode(1, l2)
                    return head
            return l2
        
        else:
            if 1 == self.sumLists(l1, l2):
                head = ListNode(1, l1)
                return head
            return l1
    
    def incrementDigit(self, node, pointer):
        if node == pointer:
            node.val += 1
        else:
            node.val += self.incrementDigit(node.next, pointer)
        if node.val > 9:
            node.val -= 10
            return 1
        return 0
    
    def sumLists(self, List1, List2):
        if not List1:
            return 0
        
        List1.val += List2.val + self.sumLists(List1.next, List2.next)
        if List1.val > 9:
            List1.val -= 10
            return 1
        return 0
    
    def getIthPointer(self, head, n):
        current = head
        while n:
            current = current.next
            n -= 1
        return current
    
    def getLength(self, head):
        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        return length
        