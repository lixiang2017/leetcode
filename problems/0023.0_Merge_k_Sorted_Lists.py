'''
heap

Runtime: 145 ms, faster than 51.71% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.9 MB, less than 53.60% of Python3 online submissions for Merge k Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        k = len(lists)
        curr = lists
        h = []
        for i in range(k):
            if curr[i]:
                heappush(h, (curr[i].val, i))
                curr[i] = curr[i].next
        
        while h:
            v, i = heappop(h)
            node.next = ListNode(val=v)
            node = node.next
            if curr[i]:
                heappush(h, (curr[i].val, i))
                curr[i] = curr[i].next
                                    
        return dummy.next


'''
Runtime: 131 ms, faster than 58.72% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.7 MB, less than 79.64% of Python3 online submissions for Merge k Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        k = len(lists)
        h = []
        for i in range(k):
            if lists[i]:
                heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while h:
            v, i = heappop(h)
            node.next = ListNode(val=v)
            node = node.next
            if lists[i]:
                heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next
                                    
        return dummy.next


'''
Runtime: 119 ms, faster than 68.20% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 18.9 MB, less than 11.10% of Python3 online submissions for Merge k Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = node = ListNode()
        h = []
        for i, l in enumerate(lists):
            if l:
                heappush(h, (l.val, i, l))
        
        while h:
            val, i, point = heappop(h)
            node.next = ListNode(val)
            node = node.next
            point = point.next
            if point:
                heappush(h, (point.val, i, point))
        
        return head.next
    

'''
heap

Runtime: 102 ms, faster than 78.21% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 17.9 MB, less than 46.85% of Python3 online submissions for Merge k Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        h = []
        for i, node in enumerate(lists):
            if node:
                heappush(h, (node.val, i, node))
        
        dummy = cur = ListNode()
        while h:
            x, i, node = heappop(h)
            nxt = node.next
            node.next = None
            cur.next = node
            cur = cur.next
            if nxt:
                heappush(h, (nxt.val, i, nxt))
        
        return dummy.next
    
