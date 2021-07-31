'''
You are here!
Your memory usage beats 54.88 % of python submissions.
'''

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.map[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for k, v in self.map.items():
            if k.startswith(prefix):
                total += v
        return total
    
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
