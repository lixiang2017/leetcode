'''
use itertools.chain and hashmap

You are here!
Your runtime beats 88.59 % of python submissions.
You are here!
Your memory usage beats 20.47 % of python submissions.

ref: 
https://docs.python.org/3/library/itertools.html#itertools.chain
https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/996476/Python-2-Solutions-explained
'''


class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        hashmap = {piece[0]: piece for piece in pieces}
        return list(chain(*[hashmap.get(num, []) for num in arr])) == arr


