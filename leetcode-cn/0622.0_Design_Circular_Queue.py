'''
list + two pointers

执行用时：68 ms, 在所有 Python3 提交中击败了81.49% 的用户
内存消耗：15.6 MB, 在所有 Python3 提交中击败了41.75% 的用户
通过测试用例：58 / 58
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k 
        self.q = [0] * k 
        self.i = 0
        self.j = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.j] = value 
        self.j = (self.j + 1) % self.k
        self.size += 1
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.i = (self.i + 1) % self.k 
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.i]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.j - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.i == self.j and self.size == 0

    def isFull(self) -> bool:
        return self.i == self.j and self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
