'''
You are here!
Your runtime beats 55.55 % of python submissions.
'''


from collections import Counter

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        size = len(A)
        union = A + B
        hashmap = Counter(union)
        hashkey = {}
        
        # for num, count in hashmap.iteritems():  
        #    if count < size:
        #        del hashmap[num]    # RuntimeError: dictionary changed size during iteration

        for num, count in hashmap.iteritems():
            if count >= size:
                hashkey[num] = count
        
        # len(hashkey)  maybe 0 1 2
        if not len(hashkey):
            return -1
        elif 1 == len(hashkey) or 2 == len(hashkey):
            key = hashkey.keys()[0]
            equal_a, equal_b = 0, 0
            for i in xrange(size):
                if key == A[i] or key == B[i]:
                    if key == A[i]:
                        equal_a += 1
                    if key == B[i]:
                        equal_b += 1
                else:
                    return -1
            return size - max(equal_a, equal_b)

        