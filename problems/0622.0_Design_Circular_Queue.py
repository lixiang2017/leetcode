'''
Runtime: 145 ms, faster than 22.42% of Python3 online submissions for Design Circular Queue.
Memory Usage: 14.3 MB, less than 98.10% of Python3 online submissions for Design Circular Queue.
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = deque(maxlen=k)        
        self.size = k
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.q.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        try:
            self.q.popleft()
            return True
        except IndexError:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.q[0]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.q[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
