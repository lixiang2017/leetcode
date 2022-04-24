'''
use array, not real linked list

Runtime: 184 ms, faster than 83.60% of Python3 online submissions for Design Linked List.
Memory Usage: 14.9 MB, less than 29.61% of Python3 online submissions for Design Linked List.
'''
class MyLinkedList:

    def __init__(self):
        self.l = []

    def get(self, index: int) -> int:
        if index >= len(self.l):
            return -1
        else:
            return self.l[index]

    def addAtHead(self, val: int) -> None:
        self.l = [val] + self.l

    def addAtTail(self, val: int) -> None:
        self.l.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.l):
            return 
        self.l = self.l[: index] + [val] + self.l[index: ]

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= len(self.l):
            return
        self.l = self.l[: index] + self.l[index + 1: ]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


