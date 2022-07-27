'''
hash map

执行用时：84 ms, 在所有 Python3 提交中击败了99.70% 的用户
内存消耗：21.5 MB, 在所有 Python3 提交中击败了98.48% 的用户
通过测试用例：20 / 20
'''
class Skiplist:

    def __init__(self):
        self.c = Counter()

    def search(self, target: int) -> bool:
        return self.c[target] > 0

    def add(self, num: int) -> None:
        self.c[num] += 1

    def erase(self, num: int) -> bool:
        if self.search(num):
            self.c[num] -= 1
            return True
        else:
            return False

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)


'''
binary search

执行用时：132 ms, 在所有 Python3 提交中击败了97.57% 的用户
内存消耗：21.3 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：20 / 20
'''
class Skiplist:

    def __init__(self):
        self.arr = []

    def search(self, target: int) -> bool:
        idx = bisect_left(self.arr, target)
        return idx != -1 and idx != len(self.arr) and self.arr[idx] == target

    def add(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def erase(self, num: int) -> bool:
        idx = bisect_left(self.arr, num)
        if idx != -1 and idx != len(self.arr) and self.arr[idx] == num:
            self.arr[idx: idx + 1] = []
            return True 
        else:
            return False

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

