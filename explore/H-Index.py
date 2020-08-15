'''
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3420/
You are here!
Your runtime beats 91.95 % of python submissions.
82 / 82 test cases passed.
    Status: Accepted
Runtime: 20 ms
Memory Usage: 13.1 MB
    
Submitted: 0 minutes ago

h_index只可能是论文的个数
'''


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_index = 0
        #if not citations:
        #    return h_index
        array = sorted(citations)
        # print 'array: ', array
        length = len(array)
        #if array[0] >= length:
        #    return length

        for i in xrange(length):
            if array[i] >= length - i:
                h_index = length - i
                break

        return h_index


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    assert Solution().hIndex(citations) == 3

    citations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Solution().hIndex(citations) == 5

    citations = [100]
    assert Solution().hIndex(citations) == 1

    citations = [99, 100]
    assert Solution().hIndex(citations) == 2

    citations = [88, 99, 100]
    assert Solution().hIndex(citations) == 3

    citations = []
    assert Solution().hIndex(citations) == 0

    citations = [4,4,0,0]
    assert Solution().hIndex(citations) == 2

    citations = [4, 0, 6, 1, 5]
    assert Solution().hIndex(citations) == 3

    citations = [0, 0, 0, 0, 0]
    assert Solution().hIndex(citations) == 0

