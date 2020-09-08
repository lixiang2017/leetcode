'''
python3 version
Success
Details
Runtime: 180 ms, faster than 94.62% of Python3 online submissions for LRU Cache.
Memory Usage: 22.7 MB, less than 95.21% of Python3 online submissions for LRU Cache.

'''

class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import collections
        self.capacity = capacity
        self.di = collections.OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.di:
            return -1
        self.di.move_to_end(key)
        return self.di[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.di[key] = value
        self.di.move_to_end(key)
        if len(self.di) > self.capacity:
            self.di.popitem(last = False)
        


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


'''
python2
AttributeError: 'OrderedDict' object has no attribute 'move_to_end'

'''

