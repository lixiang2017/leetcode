'''
simulation using single-link list 

执行用时：184 ms, 在所有 Python3 提交中击败了41.38% 的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了64.88% 的用户
通过测试用例：64 / 64
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

class MyLinkedList:

    def __init__(self):
        self.hair = Node()
        self.size = 0 

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        p = self.hair.next  
        while index:
            p = p.next 
            index -= 1
        return p.val 

    def addAtHead(self, val: int) -> None:
        prefirst = self.hair.next 
        self.hair.next = Node(val, prefirst)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        p = self.hair
        while p.next:
            p = p.next 
        p.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index < self.size:
            p = self.hair 
            while index:
                index -= 1
                p = p.next 
            post = p.next 
            p.next = Node(val, post)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        p = self.hair 
        while index:
            p = p.next 
            index -= 1
        p.next = p.next.next 
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
