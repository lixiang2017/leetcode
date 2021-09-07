'''
approach: One Pass
Time: O(N)
Space: O(1)

执行用时：24 ms, 在所有 Python 提交中击败了88.94%的用户
内存消耗：13.1 MB, 在所有 Python 提交中击败了46.14%的用户
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = cur = ListNode(val=105, next=head)
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                # use x 
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


'''
执行用时：40 ms, 在所有 Python3 提交中击败了66.31% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了9.69% 的用户
通过测试用例：166 / 166
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
需要保留cur, 把后面的都去掉
        cur    cur.next    cur.next.next
 -----> [4] -----> [7] ---------> [7] ------->[8] -------->
 先找到是否有相等元素。如果有，用x保存重复元素，依次删除之。
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = cur = ListNode(-200, head)
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                # use x  # 避免混乱
                x = cur.next.val       
                # 跳过去
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

        