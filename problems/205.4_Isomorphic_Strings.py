'''
Success
Details 
Runtime: 28 ms, faster than 73.73% of Python online submissions for Isomorphic Strings.
Memory Usage: 12.8 MB, less than 71.05% of Python online submissions for Isomorphic Strings.
'''
'''
Python map() function
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

Syntax :
map(fun, iter)

Parameters :
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
NOTE : You can pass one or more iterable to the map() function.

Returns :
Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find, s) == map(t.find, t)

if __name__ == "__main__":
    s = "egg"
    t = "add"
    assert Solution().isIsomorphic(s, t)

    s = "foo"
    t = "bar"
    assert not Solution().isIsomorphic(s, t)

    s = "paper"
    t = "title"
    assert Solution().isIsomorphic(s, t)

    # Expected false
    s = "aba"
    t = "baa"
    assert not Solution().isIsomorphic(s, t)