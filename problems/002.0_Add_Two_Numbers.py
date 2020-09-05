'''
Success
Details
Runtime: 56 ms, faster than 91.56% of Python online submissions for Add Two Numbers.
Memory Usage: 12.7 MB, less than 81.72% of Python online submissions for Add Two Numbers.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printVal(self):
        # print self.val
        reversed_list = [self.val]

        tmp = self.next
        while tmp:
            # print tmp.val
            reversed_list.append(tmp.val)
            tmp = tmp.next

        print reversed_list



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = temp = ListNode(0)
        val = 0
        while l1 or l2:
            totalVal = 0
            if l1:
                totalVal += l1.val
                l1 = l1.next
            if l2:
                totalVal += l2.val
                l2 = l2.next
            (val, remainder) = divmod(totalVal + val, 10)
            temp.next = ListNode(remainder)
            temp = temp.next

        if val > 0:
            temp.next = ListNode(val)

        return head.next
     


if __name__ == '__main__':
    l1 = ListNode(val = 2, next = ListNode(val = 4, next = ListNode(val = 3, next = None)))
    l2 = ListNode(val = 5, next = ListNode(val = 6, next = ListNode(val = 4, next = None)))
    l1.printVal()
    l2.printVal()

    totalVal = Solution().addTwoNumbers(l1, l2)
    totalVal.printVal()



