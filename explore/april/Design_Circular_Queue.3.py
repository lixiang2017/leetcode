'''
approach: Linked List
Time: O(1)
Space: O(k)

You are here!
Your runtime beats 31.99 % of python submissions.
You are here!
Your memory usage beats 57.64 % of python submissions.
'''

class Node(object):
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.elementsCnt = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        if 0 == self.elementsCnt:
            self.head = Node(value=value)
            self.tail = self.head
        else:
            self.tail.next = Node(value=value)
            self.tail = self.tail.next
        self.elementsCnt += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        bak = self.head
        self.head = self.head.next
        del bak
        self.elementsCnt -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.head.value

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.tail.value

    def isEmpty(self):
        """
        :rtype: bool
        """
        return 0 == self.elementsCnt

    def isFull(self):
        """
        :rtype: bool
        """
        return self.elementsCnt == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

