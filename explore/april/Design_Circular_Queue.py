'''
approach: List
Time: O(1)
Space :O(k)

You are here!
Your runtime beats 62.25 % of python submissions.
You are here!
Your memory usage beats 29.68 % of python submissions.
'''

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [0] * k
        self.frontPtr = 0
        self.rearPtr = 0
        self.size = k
        self.elementsCnt = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.q[self.rearPtr] = value
        self.rearPtr += 1
        self.rearPtr %= self.size
        self.elementsCnt += 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.frontPtr += 1
        self.frontPtr %= self.size
        self.elementsCnt -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.elementsCnt == 0:
            return -1
        return self.q[self.frontPtr]        

    def Rear(self):
        """
        :rtype: int
        """
        if self.elementsCnt == 0:
            return -1
        return self.q[(self.rearPtr - 1) % self.size]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return 0 == self.elementsCnt
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.elementsCnt
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

