'''
Two Pointers,Time: O(M + N),S:O(1)
执行用时：128 ms, 在所有 Python3 提交中击败了98.23% 的用户
内存消耗：29.7 MB, 在所有 Python3 提交中击败了31.97% 的用户
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        A, B = headA, headB
        while A != B:
            if not A:
                A = headB
            else:
                A = A.next
            if not B:
                B = headA            
            else:
                B = B.next
        return A

'''
8
[4,1,8,4,5]
[5,0,1,8,4,5]
2
3
2
[0,9,1,2,4]
[3,2,4]
3
1
0
[2,6,4]
[1,5]
3
2
'''


'''
0
[1,3]
[]
2
0
3
[3]
[2,3]
0
1
'''
