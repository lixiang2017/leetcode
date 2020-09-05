'''
Success
Details 
Runtime: 56 ms, faster than 38.04% of Python3 online submissions for Print FooBar Alternately.
Memory Usage: 14.2 MB, less than 32.37% of Python3 online submissions for Print FooBar Alternately.
'''

from threading import Event

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.e1 = Event()
        self.e2 = Event()
        self.e1.set()


    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            self.e1.wait()
            printFoo()
            self.e1.clear()
            self.e2.set()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
            self.e2.wait()
            printBar()
            self.e2.clear()
            self.e1.set()
