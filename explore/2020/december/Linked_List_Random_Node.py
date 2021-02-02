'''
You are here!
Your runtime beats 88.89 % of python submissions.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.length = 0
        self.back_head = head
        node = head
        while node:
            node = node.next
            self.length += 1
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        rand = random.randrange(self.length)
        node = self.back_head
        while rand:
            node = node.next
            rand -= 1
        return node.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
