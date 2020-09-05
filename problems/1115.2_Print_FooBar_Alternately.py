'''
Success
Details 
Runtime: 56 ms, faster than 16.46% of Python online submissions for Print FooBar Alternately.
Memory Usage: 13 MB, less than 33.33% of Python online submissions for Print FooBar Alternately.
'''
'''
Simple solution using two semaphores.
The basic idea:
Each function has one semaphore. Initially, the lock for the foo function should be free (since every iteration should start with it, including the first one).
After the foo function is done, it releases the bar semaphore. When the bar semaphore finishes, it releases the foo semaphore.
'''


import threading

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Semaphore(1)
        self.bar_lock = threading.Semaphore(0)


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()
