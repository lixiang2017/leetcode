'''
Success
Details 
Runtime: 32 ms, faster than 94.04% of Python3 online submissions for Print in Order.
Memory Usage: 14.2 MB, less than 10.88% of Python3 online submissions for Print in Order.
'''


from threading import Lock

class Foo:
    """ This solution uses thread locks (threading.Lock)
    """
    def __init__(self):
        self.second_locs = Lock()
        self.third_lock = Lock()
        self.second_locs.acquire()
        self.third_lock.acquire()
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_locs.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_locs.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_locs.release()
        self.third_lock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_lock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.third_lock.release()