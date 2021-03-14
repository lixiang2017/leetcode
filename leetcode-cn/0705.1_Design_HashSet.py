'''
approach: Chaining
Time: O(N / B). Supposed hash value is even, the length of every chain will be N/B.
Space: O(N + B), N is the number of elements in HashSet and B is the number of buckets.

执行用时：4008 ms, 在所有 Python 提交中击败了5.26%的用户
内存消耗：17.6 MB, 在所有 Python 提交中击败了83.46%的用户
'''


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 769
        self.bucket = [[]] * self.base

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        pos = key % self.base
        for item in self.bucket[pos]:
            if item == key:
                return
        self.bucket[pos].append(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        pos = key % self.base
        n = len(self.bucket[pos])
        for i in range(n):
            if self.bucket[pos][i] == key:
                self.bucket[pos].pop(i)
                return 


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        pos = key % self.base
        return key in self.bucket[pos]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
