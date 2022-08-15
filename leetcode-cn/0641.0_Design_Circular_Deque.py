'''
built-in list

执行用时：60 ms, 在所有 Python3 提交中击败了99.31% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了96.11% 的用户
通过测试用例：51 / 51
'''
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k 
        self.q = deque()

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        return True        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q.popleft()
        return True            

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q.pop()
        return True           

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


'''
ListNode

执行用时：76 ms, 在所有 Python3 提交中击败了43.25% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了8.92% 的用户
通过测试用例：51 / 51
'''
class ListNode:
    def __init__(self, value: int = -1, prev: ListNode = None, _next: ListNode = None):
        self.value = value 
        self.prev = prev 
        self.next = _next 

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k 
        self.dummy = ListNode()
        self.tail = self.dummy 
        self.cnt = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        n = ListNode(value)
        if self.tail == self.dummy:  # no nodes
            self.tail = n 
            self.dummy.next = n 
            self.tail.prev = self.dummy 
        else: # have nodes 
            _nxt = self.dummy.next 
            self.dummy.next = n 
            n.next = _nxt 
            _nxt.prev = n  
            n.prev = self.dummy 
        self.cnt += 1
        return True 

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        n = ListNode(value, prev = self.tail)
        self.tail.next = n
        self.tail = n  
        self.cnt += 1
        return True 

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.cnt > 1:
            self.dummy.next = self.dummy.next.next 
            self.dummy.next.prev = self.dummy
        else:
            self.dummy.next = None 
            self.tail = self.dummy 
        self.cnt -= 1
        return True        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        p = self.tail.prev 
        p.next = None 
        self.tail = p 
        self.cnt -= 1
        return True        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummy.next.value  

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.value 

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()




