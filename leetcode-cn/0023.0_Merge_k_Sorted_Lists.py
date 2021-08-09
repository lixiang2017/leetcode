'''
heapq
T: O(NKlogK)
S: O(K)

执行用时：64 ms, 在所有 Python3 提交中击败了93.35% 的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了64.80% 的用户
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # []  [[]] [[], [], []]
        if not lists:
            return None

        dummy = node = ListNode()
        h = [(l.val, id(l), l) for l in lists if l]
        heapq.heapify(h)
        while h:
            val, _id, n = heappop(h)
            # link
            node.next = n 
            node = node.next 
            if n.next:
                heappush(h, (n.next.val, id(n), n.next))

        return dummy.next

'''
TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
    heapq.heapify(h)
# using id(l) to solve it
(l.val, id(l),l)
ref:
https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue

[[1,4,5],[1,3,4],[2,6]]
[]
[[]]
[[], [], []]
[[],[1]]
'''
