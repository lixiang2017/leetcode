#! /usr/bin/env python3
'''
Success
Details 
Runtime: 40 ms, faster than 66.53% of Python3 online submissions for Print in Order.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Print in Order.
'''


import threading
class Foo:

    def __init__(self):
        self.print_lock = threading.Lock()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        with self.print_lock:
            printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.print_lock:
            printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.print_lock:
            printThird()