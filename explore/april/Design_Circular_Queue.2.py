'''
use lock

You are here!
Your runtime beats 31.99 % of python submissions.
You are here!
Your memory usage beats 29.68 % of python submissions.
'''


from threading import Lock

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [0] * k
        self.headIdx = 0
        # self.rearPtr = 0   # rearIdx = (headIdx + elementsCnt - 1) % capacity
        # self.size = k
        self.capacity = k
        self.elementsCnt = 0
        # the additional attribute to protect the access of our queue
        self.queueLock = Lock()

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # automatically acquire the lock when entering the block
        with self.queueLock:
            if self.isFull():
                return False
            self.q[(self.headIdx + self.elementsCnt) % self.capacity] = value
            # self.rearPtr += 1
            # self.rearPtr %= self.size
            self.elementsCnt += 1
        # automatically release the lock when leaving the block
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        with self.queueLock:
            if self.isEmpty():
                return False
            self.headIdx = (self.headIdx + 1) % self.capacity
            # self.frontPtr += 1
            # self.frontPtr %= self.size
            self.elementsCnt -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.elementsCnt == 0:
            return -1
        return self.q[self.headIdx]        

    def Rear(self):
        """
        :rtype: int
        """
        if self.elementsCnt == 0:
            return -1
        return self.q[(self.headIdx + self.elementsCnt - 1) % self.capacity]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return 0 == self.elementsCnt
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.capacity == self.elementsCnt
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
