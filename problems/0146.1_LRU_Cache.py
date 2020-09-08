'''
Success
Details
Runtime: 180 ms, faster than 94.62% of Python3 online submissions for LRU Cache.
Memory Usage: 22.7 MB, less than 97.13% of Python3 online submissions for LRU Cache.
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.cap = capacity
        self.n = 0
        

    def get(self, key: int) -> int:
        if key in self.d:
            value = self.d[key]
            del self.d[key]
            self.d[key] = value
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            self.d[key] = value
        else:
            self.d[key] = value
            self.n += 1

        if self.n > self.cap:
            for i in self.d:
                # print ('index: ', i)  # index:  2 # index:  1
                index = i
                break
            del self.d[index]
            self.n -= 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



if __name__ == '__main__':
    capacity = 2
    cache = LRUCache(capacity)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1       # returns 1
    cache.put(3, 3)    # evicts key 2
    assert cache.get(2) == -1       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    assert cache.get(1) == -1       # returns -1 (not found)
    assert cache.get(3) == 3       # returns 3
    assert cache.get(4) == 4       # returns 4

