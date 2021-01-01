'''
You are here!
Your runtime beats 22.46 % of python submissions.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge_sorted(list1, list2):
            cur1 = list1
            cur2 = list2
            head = ListNode(0)
            cur = head
            
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            
            if not cur1:
                cur.next = cur2
            else:
                cur.next = cur1
                
            return head.next 
        
        def getlength(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        
        def split(head, step):
            if not head:
                return None
            cur = head
            for i in xrange(step - 1):
                if cur.next:
                    cur = cur.next
            right = cur.next
            cur.next = None # to cut the link
            return right   # return the right part 
        
        # start
        if not head or not head.next:
            return head
        
        length = getlength(head)
        print 'length: ', length
        dummy = ListNode(-1)
        dummy.next = head
        
        step = 1
        while step < length:
            pre = dummy
            cur = dummy.next
            cur = pre.next
            while cur:
                h1 = cur
                h2 = split(cur, step)
                cur = split(h2, step)  # left part
                tmp = merge_sorted(h1, h2)
                pre.next = tmp   # link the former part and sorted part
                # print 'pre: ', pre
                while pre.next:
                    pre = pre.next   
            
            step *= 2   # 1 2 4 8 16 ...
        
        return dummy.next
        