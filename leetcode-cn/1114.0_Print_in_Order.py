'''
执行用时：3528 ms, 在所有 Python3 提交中击败了5.05% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了96.54% 的用户
通过测试用例：36 / 36
'''
class Foo:
    def __init__(self):
        self.order = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.order += 1

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while self.order < 1:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.order += 1

    def third(self, printThird: 'Callable[[], None]') -> None:
        while self.order < 2:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        