'''
执行用时：696 ms, 在所有 Python 提交中击败了17.74%的用户
内存消耗：15.8 MB, 在所有 Python 提交中击败了88.71%的用户
'''


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashMap[key] = value


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        return self.hashMap.get(key, -1)


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key in self.hashMap:
            self.hashMap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



'''
Runtime: 419 ms, faster than 42.15% of Python3 online submissions for Design HashMap.
Memory Usage: 40.1 MB, less than 13.37% of Python3 online submissions for Design HashMap.
'''
class MyHashMap:

    def __init__(self):
        self.m = [-1] * 1_000_005

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        return self.m[key]

    def remove(self, key: int) -> None:
        self.m[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



'''
Runtime: 289 ms, faster than 72.28% of Python3 online submissions for Design HashMap.
Memory Usage: 18.3 MB, less than 24.47% of Python3 online submissions for Design HashMap.
'''
class MyHashMap:

    def __init__(self):
        self._slot = 10001
        self._arr = [[] for _ in range(self._slot)]
    
    @property
    def size(self):
        return self._slot

    def put(self, key: int, value: int) -> None:
        e = self._encode(key)
        for i, (k, v) in enumerate(self._arr[e]):
            if k == key:
                self._arr[e].pop(i)
                break
        self._arr[e].append((key, value))
        

    def get(self, key: int) -> int:
        e = self._encode(key)
        for i, (k, v) in enumerate(self._arr[e]):
            if k == key:
                return v 
        return -1

    def remove(self, key: int) -> None:
        e = self._encode(key)
        for i, (k, v) in enumerate(self._arr[e]):
            if k == key:
                self._arr[e].pop(i)
                return
        
    def _encode(self, key: int) -> int:
        return key % self.size
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



'''
Runtime: 396 ms, faster than 47.35% of Python3 online submissions for Design HashMap.
Memory Usage: 18.3 MB, less than 30.29% of Python3 online submissions for Design HashMap.
'''
    def put(self, key: int, value: int) -> None:
        e = self._encode(key)
        Found = False
        for i, (k, v) in enumerate(self._arr[e]):
            if k == key:
                Found = True
                self._arr[e][i] = [key, value]
                break
        if not Found:
            self._arr[e].append([key, value])
        

'''
Runtime: 419 ms, faster than 42.15% of Python3 online submissions for Design HashMap.
Memory Usage: 18.2 MB, less than 30.29% of Python3 online submissions for Design HashMap.
'''
    def put(self, key: int, value: int) -> None:
        e = self._encode(key)
        Found = False
        for i, (k, v) in enumerate(self._arr[e]):
            if k == key:
                Found = True
                self._arr[e][i][1] = value
                break
        if not Found:
            self._arr[e].append([key, value])


            


