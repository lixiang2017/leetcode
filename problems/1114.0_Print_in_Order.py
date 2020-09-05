'''
Success
Details 
Runtime: 1920 ms, faster than 19.50% of Python online submissions for Print in Order.
Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Print in Order.
'''


class Foo(object):
    def __init__(self):
        self.first_executed = False
        self.second_executed = False

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_executed = True


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while not self.first_executed:
            continue

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_executed = True
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while not self.second_executed:
            continue
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
