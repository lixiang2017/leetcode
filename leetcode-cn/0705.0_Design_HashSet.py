'''

执行用时：448 ms, 在所有 Python 提交中击败了96.36%的用户
内存消耗：18.3 MB, 在所有 Python 提交中击败了69.09%的用户
'''


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashSet.add(key)


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # self.hashSet.remove(key)  # Remove an element from a set; it must be a member.  If the element is not a member, raise a KeyError.
        self.hashSet.discard(key)


    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashSet



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
