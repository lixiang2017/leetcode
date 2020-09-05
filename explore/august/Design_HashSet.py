'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3410/

28 / 28 test cases passed.
    Status: Accepted
Runtime: 152 ms
Memory Usage: 18.2 MB
    
Submitted: 0 minutes ago

You are here!
Your runtime beats 99.62 % of python submissions.
'''


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = set()
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashset:
            self.hashset.remove(key)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hashset:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



if __name__ == '__main__':
    hashSet = MyHashSet();
    hashSet.add(1);         
    hashSet.add(2);         
    assert hashSet.contains(1);    # returns true
    assert not hashSet.contains(3);    # returns false (not found)
    hashSet.add(2);          
    assert hashSet.contains(2);    # returns true
    hashSet.remove(2);          
    assert not hashSet.contains(2);    # returns false (already removed)


