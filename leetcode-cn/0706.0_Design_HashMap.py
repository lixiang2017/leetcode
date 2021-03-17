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
