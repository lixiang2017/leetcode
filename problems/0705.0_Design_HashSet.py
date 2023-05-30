'''
Runtime: 449 ms, faster than 33.16% of Python3 online submissions for Design HashSet.
Memory Usage: 40.6 MB, less than 10.21% of Python3 online submissions for Design HashSet.
'''
class MyHashSet:

    def __init__(self):
        self.h = [0] * (1_000_000 + 5)        

    def add(self, key: int) -> None:
        self.h[key] = 1

    def remove(self, key: int) -> None:
        self.h[key] = 0 

    def contains(self, key: int) -> bool:
        return self.h[key] != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



'''
Runtime: 263 ms, faster than 62.00% of Python3 online submissions for Design HashSet.
Memory Usage: 18.6 MB, less than 82.52% of Python3 online submissions for Design HashSet.
'''
class MyHashSet:

    def __init__(self):
        self.b = 0        

    def add(self, key: int) -> None:
        self.b |= 1 << key

    def remove(self, key: int) -> None:
        self.b &= ~(1 << key)

    def contains(self, key: int) -> bool:
        return bool(self.b & (1 << key))


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



'''
Runtime: 443 ms, faster than 33.47% of Python3 online submissions for Design HashSet.
Memory Usage: 18.7 MB, less than 78.48% of Python3 online submissions for Design HashSet.
'''
class MyHashSet:

    def __init__(self):
        self.b = 0        

    def add(self, key: int) -> None:
        self.b |= 1 << key

    def remove(self, key: int) -> None:
        self.b &= ~(1 << key)

    def contains(self, key: int) -> bool:
        return bool(self.b >> key & 1)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


'''
Runtime: 152 ms, faster than 80.91% of Python3 online submissions for Design HashSet.
Memory Usage: 22.4 MB, less than 23.72% of Python3 online submissions for Design HashSet.
'''
class MyHashSet:

    def __init__(self):
        self.s =  set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        self.s.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.s


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
