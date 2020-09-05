'''
Success
Details 
Runtime: 28 ms, faster than 94.94% of Python online submissions for Print FooBar Alternately.
Memory Usage: 13.1 MB, less than 20.51% of Python online submissions for Print FooBar Alternately.
'''

from threading import Lock

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()


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
