'''
S: O(N)

Runtime: 68 ms, faster than 90.58% of Python3 online submissions for Linked List Random Node.
Memory Usage: 17.2 MB, less than 97.26% of Python3 online submissions for Linked List Random Node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        self.n = len(self.nums)
        
    def getRandom(self) -> int:
        idx = random.randrange(self.n)
        return self.nums[idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


'''
S: O(N)

Runtime: 134 ms, faster than 31.61% of Python3 online submissions for Linked List Random Node.
Memory Usage: 17.5 MB, less than 23.25% of Python3 online submissions for Linked List Random Node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        self.n = len(self.nums)
        
    def getRandom(self) -> int:
        idx = random.randint(0, self.n - 1)
        return self.nums[idx]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


'''
Runtime: 72 ms, faster than 79.00% of Python3 online submissions for Linked List Random Node.
Memory Usage: 17.3 MB, less than 73.23% of Python3 online submissions for Linked List Random Node.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return choice(self.vals)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


